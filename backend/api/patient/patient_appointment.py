import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.hcw import HCW
from models.patient import Patient
from models.appointment import Appointment
from api.base import input_to_timestamp, notify, timestamp_to_str


@api.route(
    "/patient/<uuid:patientId>/appointment", methods=["GET"], strict_slashes=False
)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_patient_appointments(patientId, current_user):
    """
    Retrieves all appointments associated with a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient whose appointments are to be retrieved.
    - current_user: The authenticated user attempting to retrieve the appointments.

    Returns:
    - JSON response containing a list of appointment details.

    Raises:
    - 404: If the patient with the given patientId is not found in the database.
    - 403: If the user does not have sufficient privileges to retrieve the appointments.
    - 400: If there are input format errors in the optional start_time or end_time parameters.
    """
    # Retrieve the patient from the database using the provided patientId
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        # Return an error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404

    # Check if the user has sufficient privileges to retrieve the appointments
    if current_user.role == "patient":
        if current_user.profileId != str(patientId):
            # Return an error response if the user does not have permission to retrieve the appointments
            return {"error": "Insufficient privileges!"}, 403

    # Check the content type of the request to determine how to parse the data
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    if data:
        # Extract start_time and end_time parameters from the data, if provided
        start_time = data.get("start_time", None)
        if start_time:
            start_time = input_to_timestamp(start_time, "%Y-%m-%d %I:%M %p")
            if not start_time:
                # Return an error response if the start_time input format is invalid
                return (
                    jsonify(
                        {
                            "error": "Invalid start_time input format. Ex: 2024-08-19 08:05 AM"
                        }
                    ),
                    400,
                )

        end_time = data.get("end_time", None)
        if end_time:
            end_time = input_to_timestamp(end_time, "%Y-%m-%d %I:%M %p")
            if not end_time:
                # Return an error response if the end_time input format is invalid
                return (
                    jsonify(
                        {
                            "error": "Invalid end_time input format. Ex: 2024-08-19 08:05 AM"
                        }
                    ),
                    400,
                )

        # Retrieve appointments based on the specified time range and patientId
        res = [
            appointment.to_dict()
            for appointment in database.appt_lookup(
                start_time, end_time, patientId=str(patientId)
            )
        ]
    else:
        # If no parameters are provided, retrieve all non-archived appointments for the patient
        res = [
            appointment.to_dict()
            for appointment in patient.appointments
            if not appointment.archived
        ]

    # Return the list of appointment details in a JSON response
    return jsonify(res)


@api.route(
    "/patient/<uuid:patientId>/appointment", methods=["POST"], strict_slashes=False
)
@token_required(["doctor"])
def add_patient_appointment(patientId, current_user):
    """
    Adds a new appointment for a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient for whom the appointment is being added.
    - current_user: The authenticated user (doctor) adding the appointment.

    Request Body JSON Fields:
    - time (str): The appointment time in the format 'YYYY-MM-DD HH:MM AM/PM'.

    Returns:
    - JSON response containing the details of the newly added appointment.

    Raises:
    - 404: If the patient with the given patientId is not found in the database.
    - 400: If the time field is missing or has an invalid input format, or if the appointment time is in the past.
    """
    # Retrieve the patient from the database using the provided patientId
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        # Return an error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404

    # Determine the content type of the request to parse the data accordingly
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Extract the appointment time from the request data
    appointment_time = data.get("time", None)
    if not appointment_time:
        # Return an error response if the time field is missing
        return jsonify({"error": f"Missing time"}), 400

    # Convert the appointment time to a timestamp
    timestamp = input_to_timestamp(appointment_time, "%Y-%m-%d %I:%M %p")
    if not timestamp:
        # Return an error response if the input format of the time field is invalid
        return jsonify({"error": "Invalid input format. Ex: 19-08-2024 08:05 AM"}), 400

    # Check if the appointment time is in the past
    if timestamp < time.time():
        return jsonify({"error": "Appointment time can't be in the past"}), 400

    # Create a new appointment instance with the provided details
    appointment = Appointment(
        time=timestamp, patientId=str(patientId), hcwId=current_user.profileId
    )

    # Retrieve the healthcare worker (HCW) who created the appointment
    hcw = database.get_by_id(HCW, current_user.profileId)

    # Notify the patient about the new appointment via email or notification
    notify(
        patient.userId,
        2,
        name=f"{patient.lastName} {patient.firstName}",
        dr_name=f"{hcw.lastName} {hcw.firstName}",
        time=timestamp_to_str(timestamp, "%d-%m-%Y at %I:%M %p"),
    )

    # Return the details of the newly added appointment in a JSON response
    return jsonify(database.get_by_id(Appointment, str(appointment.id)).to_dict())
