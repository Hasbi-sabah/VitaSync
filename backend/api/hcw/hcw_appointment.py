from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.hcw import HCW
from api.base import input_to_timestamp


@api.route("/hcw/<uuid:hcwId>/appointment", methods=["POST"], strict_slashes=False)
@token_required(["doctor"])
def get_all_hcw_appointments(hcwId, current_user):
    """
    Retrieves all appointments associated with a specific hcw.

    Parameters:
    - hcwId (uuid): The unique identifier of the hcw whose appointments are to be retrieved.
    - current_user: The authenticated user attempting to retrieve the appointments.

    Returns:
    - JSON response containing a list of appointment details.

    Raises:
    - 404: If the hcw with the given hcwId is not found in the database.
    - 403: If the user does not have sufficient privileges to retrieve the appointments.
    - 400: If there are input format errors in the optional start_time or end_time parameters.
    """
    # Retrieve the hcw from the database using the provided hcwId
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        # Return an error response if the hcw is not found
        return jsonify({"error": "Health Care Worker not found"}), 404

    # Check if the user has sufficient privileges to retrieve the appointments
    if current_user.role == "doctor":
        if current_user.profileId != str(hcwId):
            # Return an error response if the user does not have permission to retrieve the appointments
            return {"error": "Insufficient privileges!"}, 403

    # Check the content type of the request to determine how to parse the data
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()
    print(data)
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

        # Retrieve appointments based on the specified time range and hcwId
        res = [
            appointment.to_dict()
            for appointment in database.appt_lookup(
                start_time, end_time, hcwId=str(hcwId)
            )
        ]
    else:
        # If no parameters are provided, retrieve all non-archived appointments for the hcw
        res = [
            appointment.to_dict()
            for appointment in hcw.appointments
            if not appointment.archived
        ]

    # Return the list of appointment details in a JSON response
    return jsonify(res)
