from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.vaccine import Vaccine


@api.route('/vaccine/<uuid:vaccineId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_vaccine(vaccineId, current_user):
    vaccine = database.get_by_id(Vaccine, str(vaccineId))
    if not vaccine:
        return jsonify({"error": "Vaccine not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != vaccine.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(vaccine.to_dict())

@api.route('/vaccine/<uuid:vaccineId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_vaccine(vaccineId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    vaccine = database.get_by_id(Vaccine, str(vaccineId))
    if not vaccine:
        return jsonify({"error": "Vaccine not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != vaccine.administeredById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    for key, value in data.items():
        if key in Vaccine.columns:
            if key == 'drugId':
                drug = database.get_by_id(Drug, str(data.get('drugId')))
                if not drug:
                    return jsonify({"error": "Drug not found"}), 404
            setattr(vaccine, key, value)
    vaccine.save()
    return jsonify(database.get_by_id(Vaccine, str(vaccineId)).to_dict())

@api.route('/vaccine/<uuid:vaccineId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_vaccine(vaccineId, current_user):
    vaccine = database.get_by_id(Vaccine, str(vaccineId))
    if not vaccine:
        return jsonify({"error": "Vaccine not found"}), 404
    vaccine.archive()
    return jsonify({})