from flask import jsonify, request
from api import api
from models import database
from models.record import Record


@api.route('/record/<uuid:recordId>', methods=['GET'], strict_slashes=False)
def get_record(recordId):
    record = database.get_by_id(Record, str(recordId))
    if not record:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(record.to_dict())

@api.route('/record/<uuid:recordId>', methods=['PUT'], strict_slashes=False)
def update_record(recordId):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    record = database.get_by_id(Record, str(recordId))
    if not record:
        return jsonify({"error": "Record not found"}), 404
    for key, value in data.items():
        if key in Record.columns:
            setattr(record, key, value)
    record.save()
    return jsonify(database.get_by_id(Record, str(recordId)).to_dict())

@api.route('/record/<uuid:recordId>', methods=['DELETE'], strict_slashes=False)
def delete_record(recordId):
    record = database.get_by_id(Record, str(recordId))
    if not record:
        return jsonify({"error": "Record not found"}), 404
    record.delete()
    return jsonify({})