from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.appointment import Appointment


@api.route('/appointment/<uuid:appointmentId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_appointment(appointmentId, current_user):
    appointment = database.get_by_id(Appointment, str(appointmentId))
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != appointment.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(appointment.to_dict())

@api.route('/appointment/<uuid:appointmentId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_appointment(appointmentId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    appointment = database.get_by_id(Appointment, str(appointmentId))
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != appointment.prescribedById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    if data.get('time', None):
        setattr(appointment, 'time', data.get('time'))
    appointment.save()
    return jsonify(database.get_by_id(Appointment, str(appointmentId)).to_dict())

@api.route('/appointment/<uuid:appointmentId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_appointment(appointmentId, current_user):
    appointment = database.get_by_id(Appointment, str(appointmentId))
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    appointment.archive()
    return jsonify({})