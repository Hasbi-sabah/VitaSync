import base64
from datetime import datetime
from io import BytesIO
from flask import app, current_app, jsonify, render_template, request, send_file, Response
import requests
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

def input_to_timestamp(input):
    input_format = "%d-%m-%Y %I:%M %p"
    try:
        datetime_obj = datetime.strptime(input, input_format)
        timestamp = int(datetime_obj.timestamp())
        return timestamp
    except ValueError:
        return None
    
def timestamp_to_str(timestamp):
    end_format = "%d-%m-%Y at %I:%M %p"
    dt_obj = datetime.fromtimestamp(timestamp)
    formatted_str = dt_obj.strftime(end_format)
    return formatted_str

def notify(userId, flag, **data): # 1 for registration for now
    user = database.get_by_id(User, objId=userId)
    if flag == 1:
        subject = 'Registration complete'
        html_content = f'<html><head></head><body><p>Hello {data["name"]},</p>You have been registered successfully</p>Here are your login credentials:</p><strong>Username:</strong> {data["username"]}</p><strong>Password:</strong> {data["password"]}</body></html>'
    elif flag == 2:
        subject = 'Appointment confirmed'
        html_content = f'<html><head></head><body><p>Hello {data["name"]},</p>Your follow up appointment with Dr. {data["dr_name"]} has been successfully booked for {data["time"]}.</body></html>'
    elif flag == 3:
        subject = 'Appointment reminder'
        html_content = f'<html><head></head><body><p>Hello {data["name"]},</p>Your appointment has been scheduled for tomorrow. Please make sure to attend at {data["time"]}.</body></html>'
    else:
        return
    if not user.email:
        return jsonify({"error": "Invalid recipient email"}), 400
    sender_name = "vitasync support"
    sender_email = current_app.config['SMTP_EMAIL']
    api_key = current_app.config["SMTP_API_KEY"]
    api_url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }
    data = {
        "sender": {
            "name": sender_name,
            "email": sender_email
        },
        "to": [
            {
                "email": user.email,
                "name": database.get_by_id(User, objId=user.profileId)
            }
        ],
        "subject": subject,
        "htmlContent": html_content
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print('sent successfully')
    else:
        print('Something Went Wrong')

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

def check_appointments():
    appointments = database.get_all('Appointment')
    timeStampNow = int(datetime.now().timestamp())
    for appointment in appointments:
        appointmentDaybefore = appointment.time - 86400
        if appointmentDaybefore < timeStampNow:
            patient = database.get_by_id(User, objId=appointment.patientId)
            patientName = f'{patient.lastName} {patient.firstName}'
            notify(appointment.patient.userId, 3, patientName=patientName, time=timestamp_to_str(appointment.time))


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
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def print_prescription(id, current_user):
    """Generate a PDF file for the given prescription ID and return it."""
    prescription = database.get_by_id(Prescription, objId=str(id))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    #Check if the current user has permission to access this prescription
    if current_user.role == 'patient' and current_user.profileId != prescription.prescribedForId:
        return {"error": "You don't have permission to access this prescription"}, 403
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
