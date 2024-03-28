from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.procedure import Procedure


@api.route("/patient/<uuid:patientId>/procedure", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_patient_procedures(patientId, current_user):
    """
    Retrieves all procedures associated with a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient whose procedures are to be retrieved.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response containing a list of dictionaries, each representing a procedure associated with the patient.

    Raises:
    - 404: If the patient with the given patientId is not found in the database.
    - 403: If the current user does not have sufficient privileges to access procedures for the patient.
    """
    # Retrieve the patient from the database using the provided patientId
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        # Return an error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404

    # Check if the current user has sufficient privileges to access procedures for the patient
    if current_user.role == "patient" and current_user.profileId != str(patientId):
        # Return an error response for insufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    # Retrieve all procedures associated with the patient from the database
    procedures = database.search(Procedure, patientId=str(patientId))

    # Convert the procedures to dictionaries and return them in a JSON response
    return jsonify([procedure.to_dict() for procedure in procedures])


@api.route(
    "/patient/<uuid:patientId>/procedure", methods=["POST"], strict_slashes=False
)
@token_required(["doctor"])
def add_patient_procedure(patientId, current_user):
    """
    Adds a new procedure for a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient for whom the procedure is being added.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response containing the details of the newly added procedure.

    Raises:
    - 404: If the patient with the given patientId is not found in the database.
    """
    # Retrieve the patient from the database using the provided patientId
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        # Return an error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404

    # Extract data from the request based on the content type
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Set the 'performedById' field if the 'status' key is present in the data
    if data.get("status", None):
        data["performedById"] = current_user.profileId

    # Create a copy of the data with only valid keys for the Procedure model
    new_data = data.copy()
    for key in data:
        if not hasattr(Procedure, key):
            new_data.pop(key, None)

    # Create a new Procedure instance with the extracted data and save it to the database
    procedure = Procedure(
        **new_data, patientId=patientId, prescribedById=current_user.profileId
    )
    return jsonify(database.get_by_id(Procedure, str(procedure.id)).to_dict())
