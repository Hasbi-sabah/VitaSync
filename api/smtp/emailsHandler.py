from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database

@api.route('/notify', methods=['POST'], strict_slashes=False)
def notify():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    email = data.get('email', None)
    if not email:
        return jsonify({"error": "Invalid email"}), 400
    subject = data.get('subject', None)
    if not subject:
        return jsonify({"error": "Invalid subject"}), 400
    message = data.get('message', None)
    if not message:
        return jsonify({"error": "Invalid message"}), 400
    # craft email and send via api
    # Sent email conf
    return jsonify({'email': "sent sucessfully"}), 200

