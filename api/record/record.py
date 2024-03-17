from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.record import Record


@api.route('/record/<uuid:recordId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient', 'admin'])
def get_record(recordId, current_user):
    record = database.get_by_id(Record, str(recordId))
    if not record:
        return jsonify({"error": "Record not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != record.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(record.to_dict())


@api.route('/record/<uuid:recordId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def update_record(recordId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    record = database.get_by_id(Record, str(recordId))
    if not record:
        return jsonify({"error": "Record not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != record.assessedById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    for key, value in data.items():
        if key in Record.columns:
            setattr(record, key, value)
    record.save()
    return jsonify(database.get_by_id(Record, str(recordId)).to_dict())


@api.route('/record/<uuid:recordId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_record(recordId, current_user):
    record = database.get_by_id(Record, str(recordId))
    if not record:
        return jsonify({"error": "Record not found"}), 404
    record.archive()
    return jsonify({})
