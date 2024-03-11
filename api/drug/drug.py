from flask import jsonify, request
from api import api
from models import database
from models.drug import Drug

@api.route('/drug', methods=['GET'] ,strict_slashes=False)
def get_all_drugs():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    if data:
        res = [drug.to_dict() for drug in database.search(Drug, **data)]
    else:
        res = [drug.to_dict() for drug in database.get_all(Drug)]
    return jsonify(res)

@api.route('/drug_lookup', methods=['GET'] ,strict_slashes=False)
def drug_lookup():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    res = [drug.to_dict() for drug in database.drug_lookup(name=data.get('n', ''))]
    return jsonify(res)

@api.route('/drug/<uuid:drugId>', methods=['GET'], strict_slashes=False)
def get_drug(drugId):
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        return jsonify({"error": "Drug not found"}), 404
    return jsonify(drug.to_dict())


@api.route('/drug', methods=['POST'], strict_slashes=False)
def add_drug():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    drug = Drug(**data)
    return jsonify(database.get_by_id(Drug, str(drug.id)).to_dict())

@api.route('/drug/<uuid:drugId>', methods=['PUT'], strict_slashes=False)
def update_drug(drugId):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        return jsonify({"error": "Drug not found"}), 404
    for key, value in data.items():
        if key in Drug.columns:
            setattr(drug, key, value)
    drug.save()
    return jsonify(database.get_by_id(Drug, str(drugId)).to_dict())

@api.route('/drug/<uuid:drugId>', methods=['DELETE'], strict_slashes=False)
def delete_drug(drugId):
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        return jsonify({"error": "Drug not found"}), 404
    drug.delete()
    return jsonify({})