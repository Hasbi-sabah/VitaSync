from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.record import Record


@api.route("/patient/<uuid:patientId>/record", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_patient_records(patientId, current_user):
    """
    Get all records for a patient by their ID.

    Args:
        patientId (uuid): The UUID of the patient whose records are to be retrieved.
        current_user: The user making the request.

    Returns:
        JSON: A JSON response containing all the patient's records that are not archived.

    Raises:
        404: If the patient with the provided ID is not found.
        403: If the user has insufficient privileges to access the patient's records.
    """
    # Retrieve the patient from the database
    patient = database.get_by_id(Patient, str(patientId))

    # Check if the patient exists
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    # Check user privileges
    if current_user.role == "patient":
        if current_user.profileId != str(patientId):
            return {"error": "Insufficient privileges!"}, 403

    # Return JSON response with all non-archived records for the patient
    return jsonify(
        [record.to_dict() for record in patient.records if not record.archived]
    )


@api.route("/patient/<uuid:patientId>/record", methods=["POST"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def add_patient_record(patientId, current_user):
    """
    Add a new record for a patient.

    Args:
        patientId (uuid): The UUID of the patient for whom the record is being added.
        current_user: The user making the request.

    Returns:
        JSON: A JSON response containing the newly added record details.

    Raises:
        404: If the patient with the provided ID is not found.
    """
    # Retrieve the patient from the database
    patient = database.get_by_id(Patient, str(patientId))

    # Check if the patient exists
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    # Determine the content type of the request data
    content_type = request.headers.get("Content-Type")

    # Process the request data based on content type
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()
    print(data)
    # Create a new record object with the provided data
    record = Record(
        diagnosis=data.get("diagnosis", None),
        notes=data.get("notes", None),
        patientId=str(patientId),
        assessedById=current_user.profileId,
    )

    # Save the new record to the database and return its details in the JSON response
    return jsonify(database.get_by_id(Record, str(record.id)).to_dict())
