from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database

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
        return jsonify({"error": "Wrong password"}), 401
    user.create_jwt()
    return jsonify({'token': user.token})

@api.route('/logout', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def logout(current_user):
    setattr(current_user, 'token', None)
    current_user.save()
    return jsonify({})
