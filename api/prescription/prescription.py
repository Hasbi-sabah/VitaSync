from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.prescription import Prescription


@api.route('/prescription/<uuid:prescriptionId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_prescription(prescriptionId, current_user):
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != prescription.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(prescription.to_dict())

@api.route('/prescription/<uuid:prescriptionId>/fill', methods=['GET'], strict_slashes=False)
@token_required(['pharmacist'])
def prescription_fill(prescriptionId, current_user):
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    if prescription.status:
        return jsonify({"error": "Prescription already filled"}), 409
    setattr(prescription, 'status', True)
    setattr(prescription, 'filledById', current_user.profileId)
    prescription.save()
    return jsonify(prescription.to_dict())

@api.route('/prescription/<uuid:prescriptionId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_prescription(prescriptionId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != prescription.assessedById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    for key, value in data.items():
        if key in Prescription.columns:
            setattr(prescription, key, value)
    prescription.save()
    return jsonify(database.get_by_id(Prescription, str(prescriptionId)).to_dict())

@api.route('/prescription/<uuid:prescriptionId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_prescription(prescriptionId, current_user):
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    if not prescription:
        return jsonify({"error": "Prescription not found"}), 404
    prescription.archive()
    return jsonify({})