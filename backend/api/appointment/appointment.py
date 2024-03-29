import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from api.base import input_to_timestamp, notify, timestamp_to_str
from models.hcw import HCW
from models import database
from models.appointment import Appointment


@api.route("/appointment/<uuid:appointmentId>", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_appointment(appointmentId, current_user):
    """
    Retrieve details of a specific appointment.

    Parameters:
    - appointmentId (uuid): The unique identifier of the appointment.

    Raises:
    - 404: If the appointment with the provided ID is not found.
    - 403: If the user does not have sufficient privileges to access the appointment.

    Returns:
    - JSON: Details of the appointment in JSON format.
    """
    # Retrieve the appointment from the database using its ID
    appointment = database.get_by_id(Appointment, str(appointmentId))

    # Check if the appointment exists
    if not appointment:
        # Return a 404 error response if the appointment is not found
        return jsonify({"error": "Appointment not found"}), 404

    # Check if the user has sufficient privileges to access the appointment
    if (
        current_user.role == "patient"
        and current_user.profileId != appointment.patient.userId
    ):
        # Return a 403 error response if the user does not have sufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    # Return details of the appointment in JSON format
    return jsonify(appointment.to_dict())


@api.route("/appointment/<uuid:appointmentId>", methods=["PUT"], strict_slashes=False)
@token_required(["doctor"])
def update_appointment(appointmentId, current_user):
    """
    Update details of a specific appointment.

    Parameters:
    - appointmentId (uuid): The unique identifier of the appointment.

    Raises:
    - 404: If the appointment with the provided ID is not found.
    - 403: If the user does not have sufficient privileges to update the appointment.
    - 400: If there are issues with the input data such as missing time or invalid format.

    Returns:
    - JSON: Updated details of the appointment in JSON format.
    """
    # Retrieve the content type of the request
    content_type = request.headers.get("Content-Type")

    # Parse the request data based on content type
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Retrieve the appointment from the database using its ID
    appointment = database.get_by_id(Appointment, str(appointmentId))

    # Check if the appointment exists
    if not appointment:
        # Return a 404 error response if the appointment is not found
        return jsonify({"error": "Appointment not found"}), 404

    # Check if the user has sufficient privileges to update the appointment
    if current_user.role != "admin":
        if current_user.profileId != appointment.hcwId:
            # Return a 403 error response if the user does not have sufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        if appointment.time < time.time():
            # Return a 403 error response if the appointment time is in the past
            return {"error": "Can't edit past appointments"}, 403

    # Check if the appointment time is provided in the request data
    appointment_time = data.get("time", None)
    if not appointment_time:
        # Return a 400 error response if the time is missing
        return jsonify({"error": f"Missing time"}), 400

    # Convert the appointment time to timestamp format
    timestamp = input_to_timestamp(appointment_time, "%Y-%m-%d %I:%M %p")
    if not timestamp:
        # Return a 400 error response if the time format is invalid
        return jsonify({"error": "Invalid input format. Ex: 19-08-2024 08:05 AM"}), 400

    # Check if the appointment time is in the past
    if timestamp < time.time():
        # Return a 400 error response if the appointment time is in the past
        return jsonify({"error": "Appointment time can't be in the past"}), 400

    # Update the appointment time and save changes
    setattr(appointment, "time", timestamp)
    appointment.save()

    # Notify the patient about the updated appointment
    notify(
        appointment.patient.userId,
        4,
        name=f"{appointment.patient.lastName} {appointment.patient.firstName}",
        dr_name=f"{appointment.hcw.lastName} {appointment.hcw.firstName}",
        time=timestamp_to_str(timestamp, "%d-%m-%Y at %I:%M %p"),
    )

    # Return the updated appointment details in JSON format
    return jsonify(database.get_by_id(Appointment, str(appointmentId)).to_dict())


@api.route(
    "/appointment/<uuid:appointmentId>", methods=["DELETE"], strict_slashes=False
)
@token_required(["doctor"])
def delete_appointment(appointmentId, current_user):
    """
    Delete a specific appointment.

    Parameters:
    - appointmentId (uuid): The unique identifier of the appointment to be deleted.

    Raises:
    - 404: If the appointment with the provided ID is not found.
    - 403: If the user does not have sufficient privileges to delete the appointment.

    Returns:
    - JSON: An empty JSON response indicating successful deletion.
    """
    # Retrieve the appointment from the database using its ID
    appointment = database.get_by_id(Appointment, str(appointmentId))

    # Check if the appointment exists
    if not appointment:
        # Return a 404 error response if the appointment is not found
        return jsonify({"error": "Appointment not found"}), 404

    # Check if the user has sufficient privileges to delete the appointment
    if current_user.role != "admin":
        if current_user.profileId != appointment.hcwId:
            # Return a 403 error response if the user does not have sufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        if appointment.time < time.time():
            # Return a 403 error response if the appointment time is in the past
            return {"error": "Can't edit past appointments"}, 403

    # Archive the appointment (soft delete)
    appointment.archive()

    # Notify the patient about the deleted appointment
    notify(
        appointment.patient.userId,
        5,
        name=f"{appointment.patient.lastName} {appointment.patient.firstName}",
        dr_name=f"{appointment.hcw.lastName} {appointment.hcw.firstName}",
        time=timestamp_to_str(appointment.time, "%d-%m-%Y at %I:%M %p"),
    )

    # Return an empty JSON response indicating successful deletion
    return jsonify({})
