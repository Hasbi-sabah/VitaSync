from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.vital import Vital


@api.route('/vital/<uuid:vitalId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_vital(vitalId, current_user):
    vital = database.get_by_id(Vital, str(vitalId))
    if not vital:
        return jsonify({"error": "Vital take not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != vital.takenFor.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(vital.to_dict())

@api.route('/vital/<uuid:vitalId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def update_vital(vitalId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    vital = database.get_by_id(Vital, str(vitalId))
    if not vital:
        return jsonify({"error": "Vital take not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != vital.takenById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    for key, value in data.items():
        if key in Vital.columns:
            setattr(vital, key, value)
    vital.save()
    return jsonify(database.get_by_id(Vital, str(vitalId)).to_dict())

@api.route('/vital/<uuid:vitalId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_vital(vitalId, current_user):
    vital = database.get_by_id(Vital, str(vitalId))
    if not vital:
        return jsonify({"error": "Vital take not found"}), 404
    vital.archive()
    return jsonify({})