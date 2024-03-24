from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.record import Record


@api.route('/patient/<uuid:patientId>/record', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_records(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([record.to_dict() for record in patient.records])

@api.route('/patient/<uuid:patientId>/record', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def add_patient_record(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    record = Record(**data, patientId=patientId, assessedById=current_user.profileId)
    return jsonify(database.get_by_id(Record, str(record.id)).to_dict())
