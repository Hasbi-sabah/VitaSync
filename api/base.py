from flask import jsonify, request, send_file
import qrcode
from api import api
from models import database

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
    