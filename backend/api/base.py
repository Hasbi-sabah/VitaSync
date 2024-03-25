import base64
from datetime import datetime, timedelta
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
from models.appointment import Appointment
from models.drug_prescribed import DrugPrescribed
from api.auth_middleware import token_required

def input_to_timestamp(input):
    """
    Convert a string input representing a date and time to a Unix timestamp.

    This function takes a string input in the format "dd-mm-yyyy hh:mm AM/PM"
    and converts it into a Unix timestamp.
    """
    input_format = "%d-%m-%Y %I:%M %p"  # Format of the input string
    try:
        # Attempt to parse the input string into a datetime object
        datetime_obj = datetime.strptime(input, input_format)
        # Convert the datetime object to a Unix timestamp (integer)
        timestamp = int(datetime_obj.timestamp())
        return timestamp  # Return the Unix timestamp
    except ValueError:
        # If the input string is not in the correct format, return None
        return None
    
def timestamp_to_str(timestamp):
    """
    Convert a Unix timestamp to a formatted date and time string.

    This function takes a Unix timestamp and converts it into a formatted string representing a date and time.
    """
    end_format = "%d-%m-%Y at %I:%M %p"  # Desired format for the date and time string
    dt_obj = datetime.fromtimestamp(timestamp)  # Convert the timestamp to a datetime object
    formatted_str = dt_obj.strftime(end_format)  # Format the datetime object into a string
    return formatted_str  # Return the formatted date and time string

def notify(userId, flag, **data):
    """
    Send an email notification to a user based on the specified flag.

    This function sends an email notification to a user identified by their user ID.
    The flag determines the type of notification to send, and the data dictionary
    contains information specific to each type of notification.
    """
    # Retrieve the user information from the database
    user = database.get_by_id(User, objId=userId)
    
    # Determine the subject and HTML content based on the flag
    if flag == 1:
        subject = 'Registration complete'
        html_content = f'<html><head></head><body><p>Hello {data["name"]},</p>You have been registered successfully</p>Here are your login credentials:</p><strong>Username:</strong> {data["username"]}</p><strong>Password:</strong> {data["password"]}</body></html>'
    elif flag == 2:
        subject = 'Appointment confirmed'
        html_content = f'<html><head></head><body><p>Hello {data["name"]},</p>Your follow up appointment with Dr. {data["dr_name"]} has been successfully booked for {data["time"]}.</body></html>'
    elif flag == 3:
        subject = 'Appointment reminder'
        html_content = f'<html><head></head><body><p>Hello {data["name"]},</p>You have an appointment scheduled for tomorrow with Dr. {data["dr_name"]}. Please make sure to attend at {data["time"]}.</body></html>'
    else:
        return
    
    # Check if the user's email is valid
    if not user.email:
        return jsonify({"error": "Invalid recipient email"}), 400
    
    # Configure email sender details
    sender_name = "VitaSync Support"
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
    
    # Send the email using the Brevo API
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print('sent successfully')
    else:
        print('Something Went Wrong')

def make_qr(id):
    """
    Generate a QR code image for the specified ID.

    This function creates a QR code image using the qrcode library based on the provided ID.
    The QR code contains the ID encoded within it.
    """
    # Initialize a QR code object with specified parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the ID data to the QR code
    qr.add_data(id)
    qr.make(fit=True)
    
    # Generate the QR code image with black fill color and white background color
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert the image to bytes and store it in BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes)
    img_bytes.seek(0)
    
    # Return the BytesIO object containing the QR code image
    return img_bytes

def check_appointments():
    """
    Check and notify patients about upcoming appointments.

    This function checks for upcoming appointments within the next 24 hours and notifies the patients
    about their scheduled appointments through email reminders.
    """
    # Calculate the timestamp for tomorrow
    timingint = datetime.now() + timedelta(days=1)
    timeStampAfter = timingint.timestamp()
    timeStampNow = int(datetime.now().timestamp())
    
    # Lookup upcoming appointments in the database
    upcoming_appointments = database.appt_lookup(timeStampNow, timeStampAfter)

    # Iterate through the upcoming appointments
    with current_app.app_context():
        for appointment in upcoming_appointments:
            patient = appointment.patient
            if patient:
                # Extract patient and doctor names
                patientName = f'{patient.lastName} {patient.firstName}'
                drName = f'{appointment.hcw.lastName} {appointment.hcw.firstName}'
                
                # Notify the patient about the appointment reminder
                notify(patient.userId, 3, name=patientName, dr_name=drName, time=timestamp_to_str(appointment.time))


@api.route('/get_qr/<uuid:id>', methods=['GET'], strict_slashes=False)
def get_qr(id):
    """
    Generate a QR code for the given ID and return the URL to the QR code image.

    :param id: ID of the object for which the QR code is generated.
    :return: attachement of the generated QR code image.
    :raises 404: If the object with the specified ID is not found in the database.
    """
    inst = database.get_by_id(objId=str(id))
    if not inst:
        return jsonify({"error": "Not found"}), 404

    # Generate QR code image bytes
    img_bytes = make_qr(id)

    # Return the QR code image as an attachment
    return send_file(img_bytes, mimetype='image/png', as_attachment=True, download_name=f'qr_code_{id}.png')


@api.route('/print_prescription/<uuid:id>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def print_prescription(id, current_user):
    """
    Generate a PDF file for the given prescription ID and return it.

    :param id: ID of the prescription for which the PDF is generated.
    :param current_user: Current authenticated user (obtained from token).
    :return: PDF file containing the prescription details.
    :raises 404: If the prescription with the specified ID is not found in the database.
    :raises 403: If the user does not have permission to access the prescription.
    """
    prescription = database.get_by_id(Prescription, objId=str(id))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404

    # Check if the current user has permission to access this prescription
    if current_user.role == 'patient' and current_user.profileId != prescription.prescribedForId:
        return {"error": "You don't have permission to access this prescription"}, 403

    # Render the prescription details into HTML template
    rendered_template = render_template('file.html', prescription=prescription,
                                        patient=prescription.prescribedFor,
                                        doc=prescription.prescribedBy,
                                        drugs=prescription.drugs,
                                        qr=base64.b64encode(make_qr(prescription.id).getvalue()).decode('utf-8'))

    # Generate PDF from the HTML template
    css = CSS(string=''' @page {size: 315mm 445.5mm;} ''')
    pdf = HTML(string=rendered_template).write_pdf(stylesheets=[css])

    # Return the PDF file with appropriate headers
    return Response(pdf, mimetype='application/pdf', headers={
        'Content-Disposition': 'attachment; filename=prescription.pdf'
    })
