from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.prescription import Prescription
from models.drug_prescribed import DrugPrescribed

@api.route('/prescription/<uuid:prescriptionId>/drug', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_prescription_drugs(prescriptionId, current_user):
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != prescription.prescribedForId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([drug.to_dict() for drug in prescription.drugs])

@api.route('/prescription/<uuid:prescriptionId>/drug', methods=['POST'], strict_slashes=False)
@token_required(['doctor'])
def add_prescription_drug(prescriptionId, current_user):
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    content_type = request.headers.get('Content-Type')
    data = request.get_json() if content_type == 'application/json' else request.form.to_dict()
    for attr in DrugPrescribed.columns:
        if not data.get(attr, None):
            return jsonify({"error": f"Missing {attr}"}), 400
    drug = database.get_by_id(Drug, str(data.get('drugId')))
    if not drug:
        return jsonify({"error": "Drug not found"}), 404
    drug = DrugPrescribed(**data, prescriptionId=prescriptionId)
    return jsonify(database.get_by_id(DrugPrescribed, str(drug.id)).to_dict())
