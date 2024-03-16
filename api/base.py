from io import BytesIO
from flask import jsonify, render_template, request, send_file
from weasyprint import HTML
import qrcode
from api import api
from models import database
from models.prescription import Prescription

@api.route('/get_qr/<uuid:id>', methods=['GET'], strict_slashes=False)
def get_qr(id):
    inst = database.get_by_id(objId=str(id))
    if not inst:
        return jsonify({"error": "Not found"}), 404
    
    filename = f"qr_codes/{id}.png"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(id)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    return send_file(filename, as_attachment=True)
    
@api.route('/print_prescription/<uuid:id>', methods=['GET'], strict_slashes=False)
def print_prescription(id):
    prescription = database.get_by_id(Prescription, objId=str(id))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    return render_template('file.html', prsc=prescription)
    # rendered = render_template('file.html', prsc=prescription)
    # pdf_data = HTML(string=rendered).write_pdf()

    # # Create a BytesIO object to store the PDF data
    # pdf_buffer = BytesIO(pdf_data)

    # # Send the PDF file as a downloadable attachment
    # return send_file(pdf_buffer, download_name='printed_document.pdf', as_attachment=True)
    