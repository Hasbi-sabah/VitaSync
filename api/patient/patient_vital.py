from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.vital import Vital

@api.route('/patient/<uuid:patientId>/vital', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_vitals(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([vital.to_dict() for vital in database.search(Vital, patientId=str(patientId))])

@api.route('/patient/<uuid:patientId>/vital', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def add_patient_vital(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    vital = Vital(**data, takenForId=patientId, takenById=current_user.profileId)
    return jsonify(database.get_by_id(Vital, str(vital.id)).to_dict())