from flask import jsonify, request
from api import api
from models import database
from models.hcw import HCW
from models.user import User

@api.route('/hcw', methods=['GET'] ,strict_slashes=False)
def get_all_hcws():
    res = []
    for hcw in database.get_all(HCW):
        hcw_dict = hcw.to_dict()
        hcw_dict.update(database.get_by_id(User, str(hcw.userId)).to_dict())
        res.append(hcw_dict)
    return jsonify(res)

@api.route('/hcw/<uuid:hcwId>', methods=['GET'], strict_slashes=False)
def get_hcw(hcwId):
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404
    return jsonify(hcw.to_dict())


@api.route('/hcw', methods=['POST'], strict_slashes=False)
def add_hcw():
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
def update_hcw(hcwId):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404
    for key, value in data.items():
        if key in HCW.columns:
            setattr(hcw, key, value)
    hcw.save()
    return jsonify(database.get_by_id(HCW, str(hcwId)).to_dict())

@api.route('/hcw/<uuid:hcwId>', methods=['DELETE'], strict_slashes=False)
def delete_hcw(hcwId):
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404
    hcw.delete()
    return jsonify({})

