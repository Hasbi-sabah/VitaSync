from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.procedure import Procedure


@api.route('/procedure/<uuid:procedureId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_procedure(procedureId, current_user):
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        return jsonify({"error": "Procedure not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != procedure.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(procedure.to_dict())

@api.route('/procedure/<uuid:procedureId>/perform', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse'])
def procedure_fill(procedureId, current_user):
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        return jsonify({"error": "Procedure not found"}), 404
    if procedure.status:
        return jsonify({"error": "Procedure already performed"}), 409
    setattr(procedure, 'status', True)
    setattr(procedure, 'performedById', current_user.profileId)
    procedure.save()
    return jsonify(procedure.to_dict())

@api.route('/procedure/<uuid:procedureId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_procedure(procedureId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        return jsonify({"error": "Procedure not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != procedure.prescribedById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    for key, value in data.items():
        if key in Procedure.columns:
            setattr(procedure, key, value)
    procedure.save()
    return jsonify(database.get_by_id(Procedure, str(procedureId)).to_dict())

@api.route('/procedure/<uuid:procedureId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_procedure(procedureId, current_user):
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        return jsonify({"error": "Procedure not found"}), 404
    procedure.archive()
    return jsonify({})