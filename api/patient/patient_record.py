from flask import jsonify, request
from api import api
from models import database
from models.patient import Patient
from models.record import Record

@api.route('/patient/<uuid:patientId>/record', methods=['GET'], strict_slashes=False)
def get_all_patient_records(patientId):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify([record.to_dict() for record in patient.records])