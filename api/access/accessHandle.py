from flask import jsonify, request
from api import api
from models import database
from models.hcw import HCW
from models.patient import Patient
from models.user import User

@api.route('/login', methods=['POST'], strict_slashes=False)
def login():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    username = data.get('username', None)
    if not username:
        return jsonify({"error": "Invalid Credentials"}), 400
    password = data.get('password', None)
    if not password:
       return jsonify({"error": "invalid credentials"}), 400
    user = database.get_by_username(username=username)
    if not user:
        return jsonify({"error": "User does not found"}), 404
    if not user.check_hash(password):
        return jsonify({"error": "invalid credentials"}), 401
    profile = database.get_profile(user.profileId)
    print(profile)
    return jsonify(profile.to_dict())
