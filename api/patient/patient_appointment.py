from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.hcw import HCW
from models.patient import Patient
from models.appointment import Appointment
from api.base import input_to_timestamp, notify, timestamp_to_str
from models.user import User

@api.route('/patient/<uuid:patientId>/appointment', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_appointments(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([appointment.to_dict() for appointment in patient.appointments])

@api.route('/patient/<uuid:patientId>/appointment', methods=['POST'], strict_slashes=False)
@token_required(['doctor'])
def add_patient_appointment(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    time = data.get('time', None)
    if not time:
        return jsonify({"error": f"Missing time"}), 400
    timestamp = input_to_timestamp(time)
    if not timestamp:
        return jsonify({"error": "Invalid input format. Ex: 19-08-2024 08:05 AM"}), 400
    appointment = Appointment(time=timestamp, patientId=patientId, hcwId=current_user.profileId)
    hcw = database.get_by_id(HCW, current_user.profileId)
    # notify(patient.userId, 2, name=f'{patient.lastName} {patient.firstName}', dr_name=f'{hcw.lastName} {hcw.firstName}', time=timestamp_to_str(timestamp))
    return jsonify(database.get_by_id(Appointment, str(appointment.id)).to_dict())
