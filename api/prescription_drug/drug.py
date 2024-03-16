from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.drug_prescribed import DrugPrescribed


@api.route('/prescription_drug/<uuid:drugId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_prescription_drug(drugId, current_user):
    drug = database.get_by_id(DrugPrescribed, str(drugId))
    if not drug:
        return jsonify({"error": "Prescription drug not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != drug.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(drug.to_dict())

@api.route('/prescription_drug/<uuid:drugId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_prescription_drug(drugId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    drug = database.get_by_id(DrugPrescribed, str(drugId))
    if not drug:
        return jsonify({"error": "Prescription drug not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != drug.prescription.prescribedById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    for key, value in data.items():
        if key in DrugPrescribed.columns:
            if key == 'drugId':
                drug = database.get_by_id(Drug, str(data.get('drugId')))
                if not drug:
                    return jsonify({"error": "Drug not found"}), 404
            setattr(drug, key, value)
    drug.save()
    return jsonify(database.get_by_id(DrugPrescribed, str(drugId)).to_dict())

@api.route('/prescription_drug/<uuid:drugId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_prescription_drug(drugId, current_user):
    drug = database.get_by_id(DrugPrescribed, str(drugId))
    if not drug:
        return jsonify({"error": "Prescription drug not found"}), 404
    drug.archive()
    return jsonify({})