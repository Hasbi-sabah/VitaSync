from flask import jsonify, request
from api import api
from api.base import notify
from models import database
from models.patient import Patient
from models.user import User
from api.auth_middleware import token_required


@api.route('/patient_extended', methods=['GET'] ,strict_slashes=False)
@token_required([])
def get_all_extended_patients(current_user):
    res = []
    for patient in database.get_all(Patient):
        patient_dict = patient.to_dict()
        user_dict = database.get_by_id(User, str(patient.userId)).to_dict()
        user_dict.pop('id', None)
        patient_dict.update(user_dict)
        res.append(patient_dict)
    return jsonify(res)


@api.route('/patient', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def get_all_patients(current_user):
    res = [patient.to_dict() for patient in database.get_all(Patient)]
    return jsonify(res)


@api.route('/patient/<uuid:patientId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_patient(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(patient.to_dict())


@api.route('/patient_extended/<uuid:patientId>', methods=['GET'], strict_slashes=False)
@token_required(['patient'])
def get_patient_extended(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    patient_dict = patient.to_dict()
    user_dict = database.get_by_id(User, str(patient.userId)).to_dict()
    user_dict.pop('id', None)
    patient_dict.update(user_dict)
    return jsonify(patient_dict)


@api.route('/patient', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def add_patient(current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    for attr in Patient.columns[:-2]:
        if not data.get(attr, None):
            return jsonify({"error": f"Missing {attr}"}), 400
    if data.get('username', None) and database.search(User, username=data.get('username')):
        return jsonify({"error": "Username already exists in database"}), 409
    if database.search(User, email=data.get('email', None)):
        return jsonify({"error": "Email already exists in database"}), 409
    data['role'] = 'patient'
    patient = Patient(**data)
    # notify(patient.userId, 1, name=f'{patient.lastName} {patient.firstName}', username=database.get_by_id(User, str(patient.userId)).username, password=data['password'])
    return jsonify(database.get_by_id(Patient, str(patient.id)).to_dict())


@api.route('/patient/<uuid:patientId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def update_patient(patientId, current_user):
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
@token_required([])
def delete_patient(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
        user = database.get_by_id(User, hcw.userId)
    user = database.get_by_id(User, patient.userId)
    patient.archive()
    user.archive()
    return jsonify({})
