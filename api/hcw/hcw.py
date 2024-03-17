from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.hcw import HCW
from models.user import User


@api.route('/hcw_extended', methods=['GET'] ,strict_slashes=False)
@token_required([])
def get_all_extended_hcws(current_user):
    res = []
    for hcw in database.get_all(HCW):
        hcw_dict = hcw.to_dict()
        user_dict = database.get_by_id(User, str(hcw.userId)).to_dict()
        user_dict.pop('id', None)
        hcw_dict.update(user_dict)
        res.append(hcw_dict)
    return jsonify(res)


@api.route('/hcw', methods=['GET'] ,strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_hcws(current_user):
    res = [hcw.to_dict() for hcw in database.get_all(HCW)]
    return jsonify(res)


@api.route('/hcw_extended/<uuid:hcwId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def get_hcw_extended(hcwId, current_user):
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != str(hcwId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    hcw_dict = hcw.to_dict()
    user_dict = database.get_by_id(User, str(hcw.userId)).to_dict()
    user_dict.pop('id', None)
    hcw_dict.update(user_dict)
    return jsonify(hcw_dict)


@api.route('/hcw/<uuid:hcwId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def get_hcw(hcwId, current_user):
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != str(hcwId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(hcw.to_dict())


@api.route('/hcw', methods=['POST'], strict_slashes=False)
@token_required([])
def add_hcw(current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    for attr in HCW.columns:
        if not data.get(attr, None):
            return jsonify({"error": f"Missing {attr}"}), 400
    if database.search(HCW, licence=data.get('licence', None)):
        return jsonify({"error": "License already exists in database"}), 409
    hcw = HCW(**data)
    return jsonify(database.get_by_id(HCW, str(hcw.id)).to_dict())


@api.route('/hcw/<uuid:hcwId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def update_hcw(hcwId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != str(hcwId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    for key, value in data.items():
        if key in HCW.columns:
            setattr(hcw, key, value)
    hcw.save()
    return jsonify(database.get_by_id(HCW, str(hcwId)).to_dict())


@api.route('/hcw/<uuid:hcwId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_hcw(hcwId, current_user):
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != str(hcwId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    hcw.archive()
    return jsonify({})

