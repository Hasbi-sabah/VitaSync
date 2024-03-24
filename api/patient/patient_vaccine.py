from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.patient import Patient
from models.vaccine import Vaccine

@api.route('/patient/<uuid:patientId>/vaccine', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_vaccines(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([vaccine.to_dict() for vaccine in patient.vaccines])

@api.route('/patient/<uuid:patientId>/vaccine', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse'])
def add_patient_vaccine(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    if not data.get('drugId', None):
        return jsonify({"error": "Missing drug ID"}), 400
    drug = database.get_by_id(Drug, str(data.get('drugId')))
    if not drug:
        return jsonify({"error": "Drug not found"}), 404
    vaccine = Vaccine(**data, administeredForId=patientId, administeredById=current_user.profileId)
    return jsonify(database.get_by_id(Vaccine, str(vaccine.id)).to_dict())