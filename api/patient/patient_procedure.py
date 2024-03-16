from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.procedure import Procedure

@api.route('/patient/<uuid:patientId>/procedure', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_procedures(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([procedure.to_dict() for procedure in database.search(Procedure, patientId=str(patientId))])

@api.route('/patient/<uuid:patientId>/procedure', methods=['POST'], strict_slashes=False)
@token_required(['doctor'])
def add_patient_procedure(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    if data.get('status', None):
        data['administeredById'] = current_user.profileId
    procedure = Procedure(**data, patientId=patientId, prescribedById=current_user.profileId)
    return jsonify(database.get_by_id(Procedure, str(procedure.id)).to_dict())