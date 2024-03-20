from flask import jsonify, request, current_app
import requests
from api import api
from api.auth_middleware import token_required
from models import database


@api.route('/notify', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'pharmacist', 'admin'])
def notify(current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    to_email = data.get('to_email', None)
    to_name = data.get('to_name', 'John Doe')
    subject = data.get('subject', 'Hi!')
    html_content = data.get('html_content', '<html><head></head><body><p>Hello,</p>This is my first transactional email sent from Brevo.</p></body></html>')
    if not to_email:
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
                "email": to_email,
                "name": to_name
            }
        ],
        "subject": subject,
        "htmlContent": html_content
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return jsonify({'email': "sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send email", "status_code": response.status_code}), 500
