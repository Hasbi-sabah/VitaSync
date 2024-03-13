from flask import jsonify, request
from api import api
from models import database
from models.patient import Patient
from models.user import User

@api.route('/patient_extended', methods=['GET'] ,strict_slashes=False)
def get_all_extended_patients():
    res = []
    for patient in database.get_all(Patient):
        patient_dict = patient.to_dict()
        patient_dict.update(database.get_by_id(User, str(patient.userId)).to_dict())
        res.append(patient_dict)
    return jsonify(res)

@api.route('/patient', methods=['GET'] ,strict_slashes=False)
def get_all_patients():
    res = [patient.to_dict() for patient in database.get_all(Patient)]
    return jsonify(res)

@api.route('/patient/<uuid:patientId>', methods=['GET'], strict_slashes=False)
def get_patient(patientId):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patient.to_dict())

@api.route('/patient_extended/<uuid:patientId>', methods=['GET'], strict_slashes=False)
def get_patient_extended(patientId):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    patient_dict = patient.to_dict()
    user_dict = database.get_by_id(User, str(patient.userId)).to_dict()
    user_dict.pop('id', None)
    patient_dict.update(user_dict)
    return jsonify(patient_dict)

@api.route('/patient', methods=['POST'], strict_slashes=False)
def add_patient():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    for attr in Patient.columns[:-2]:
        if not data.get(attr, None):
            return jsonify({"error": f"Missing {attr}"}), 400
    patient = Patient(**data)
    return jsonify(database.get_by_id(Patient, str(patient.id)).to_dict())

@api.route('/patient/<uuid:patientId>', methods=['PUT'], strict_slashes=False)
def update_patient(patientId):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    for key, value in data.items():
        if key in Patient.columns:
            setattr(patient, key, value)
    patient.save()
    return jsonify(database.get_by_id(Patient, str(patientId)).to_dict())

@api.route('/patient/<uuid:patientId>', methods=['DELETE'], strict_slashes=False)
def delete_patient(patientId):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    patient.delete()
    return jsonify({})

