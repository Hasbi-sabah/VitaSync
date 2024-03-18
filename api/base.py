import base64
from io import BytesIO
from flask import jsonify, render_template, request, send_file, Response
from weasyprint import CSS, HTML
import qrcode
from api import api
from models import database
from models.prescription import Prescription
from models.hcw import HCW
from models.user import User
from models.drug import Drug
from models.drug_prescribed import DrugPrescribed
from api.auth_middleware import token_required

def make_qr(id):
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
    return img_bytes

@api.route('/get_qr/<uuid:id>', methods=['GET'], strict_slashes=False)
def get_qr(id):
    """Generate a QR code for the given ID and return the URL to the QR code image."""
    inst = database.get_by_id(objId=str(id))
    if not inst:
        return jsonify({"error": "Not found"}), 404
    img_bytes = make_qr(id)
    return send_file(img_bytes, mimetype='image/png', as_attachment=True, download_name=f'qr_code_{id}.png')
    # return jsonify({"qr_code_url": request.url_root + f"qr_codes/{id}.png"})


@api.route('/print_prescription/<uuid:id>', methods=['GET'], strict_slashes=False)
# @token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def print_prescription(id):
    """Generate a PDF file for the given prescription ID and return it."""
    prescription = database.get_by_id(Prescription, objId=str(id))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    # Check if the current user has permission to access this prescription
    # if current_user.role == 'patient' and current_user.profileId != prescription.prescribedForId:
    #     return {"error": "You don't have permission to access this prescription"}, 403
    rendered_template = render_template('file.html', prescription=prescription,
                                        patient=prescription.prescribedFor,
                                        doc=prescription.prescribedBy,
                                        drugs=prescription.drugs,
                                        qr=base64.b64encode(make_qr(prescription.id).getvalue()).decode('utf-8'))
    # composing html to pdf based on previous func's logic by sabah
    css = CSS(string=''' @page {size: 315mm 445.5mm;} ''')
    pdf = HTML(string=rendered_template).write_pdf(stylesheets=[css])
    #Return PDF file with appropriate headers
    return Response(pdf, mimetype='application/pdf', headers={
        'Content-Disposition': 'attachment; filename=prescription.pdf'
    })
