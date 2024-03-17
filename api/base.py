from io import BytesIO
from flask import jsonify, render_template, request, send_file, Response
from weasyprint import HTML
import qrcode
from api import api
from models import database
from models.prescription import Prescription
from models.hcw import HCW
from models.user import User
from models.drug import Drug
from models.drug_prescribed import DrugPrescribed
from api.auth_middleware import token_required

@api.route('/get_qr/<uuid:id>', methods=['GET'], strict_slashes=False)
def get_qr(id):
    """Generate a QR code for the given ID and return the URL to the QR code image."""
    inst = database.get_by_id(objId=str(id))
    if not inst:
        return jsonify({"error": "Not found"}), 404
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes)
    img_bytes.seek(0)
    return jsonify({"qr_code_url": request.url_root + f"qr_codes/{id}.png"})


@api.route('/print_prescription/<uuid:id>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def print_prescription(id, current_user):
    """Generate a PDF file for the given prescription ID and return it."""
    prescription = database.get_by_id(Prescription, objId=str(id))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    # Check if the current user has permission to access this prescription
    if current_user.role == 'patient' and current_user.profileId != prescription.prescribedForId:
        return {"error": "You don't have permission to access this prescription"}, 403
    getPrescribedBy = database.get_by_id(HCW, prescription.prescribedById)
    drugs = []
    for drug_prescribed in prescription.drugs:
        drug = database.get_by_id(Drug, drug_prescribed.drugId)
        drugs.append({
            "name": drug.commercialName,
            "form": drug.form,
            "dose": drug.dose,
            "price": drug.price
        })
    data = {
        "id": prescription.id,
        "patient": current_user.username,
        "doc": f"Dr. {getPrescribedBy.firstName} {getPrescribedBy.lastName}",
        "drugs": drugs
    }
    # dear yassine render the template with prescription data
    rendered_template = render_template('file.html', data=data)
    # composing html to pdf based on previous func's logic by sabah
    pdf = HTML(string=rendered_template).write_pdf()
    #Return PDF file with appropriate headers
    return Response(pdf, mimetype='application/pdf', headers={
        'Content-Disposition': 'attachment; filename=prescription.pdf'
    })
