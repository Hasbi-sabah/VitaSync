from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.med_info import MedInfo


@api.route("/patient/<uuid:patientId>/info", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_patient_infos(patientId, current_user):
    """
    Get all medical information of a patient.

    Parameters:
        patientId (uuid): The ID of the patient whose information is to be retrieved.
        current_user: The user making the request with appropriate authorization token.

    Returns:
        A JSON response containing the medical information of the patient if found, or an empty object if no information is available.

    Raises:
        404: If the specified patient ID is not found.
        403: If the user has insufficient privileges to access the patient's information.
    """
    # Retrieve the patient using the provided patientId
    patient = database.get_by_id(Patient, str(patientId))

    # Check if the patient exists
    if not patient:
        # Raise a 404 error if the patient is not found
        return jsonify({"error": "Patient not found"}), 404

    # Check user privileges for accessing patient information
    if current_user.role == "patient" and current_user.profileId != str(patientId):
        # Raise a 403 error if the user has insufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    # Check if the patient has medical information and it is not archived and return the medical information of the patient as a JSON response
    return jsonify(
        patient.medicalInfo.to_dict()
        if patient.medicalInfo and not patient.medicalInfo.archived
        else {}
    )


@api.route("/patient/<uuid:patientId>/info", methods=["POST"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def add_patient_info(patientId, current_user):
    """
    Add medical information for a patient.

    Args:
        patientId (uuid): The UUID of the patient to add medical information for.
        current_user: The user making the request (doctor, nurse, or pharmacist).

    Returns:
        JSON: A JSON response containing the newly added medical information.

    Raises:
        404: If the patient with the provided ID is not found.
        400: If the patient already has medical information that is not archived.

    Note:
        This endpoint is accessible to doctors, nurses, and pharmacists with valid tokens.
    """
    # Retrieve the patient from the database
    patient = database.get_by_id(Patient, str(patientId))

    # Check if the patient exists
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    # Determine the content type of the request
    content_type = request.headers.get("Content-Type")

    # Process the incoming data based on content type
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    
    # Check if the patient already has medical information
    if patient.medicalInfo and not patient.medicalInfo.archived:
        # Update the medical information attributes based on the request data
        for key, value in data.items():
            # Check if the requesting user is not an admin and if the key is in restricted fields
            if current_user.role != "admin" and key in [
                "id",
                "created_at",
                "modified_at",
                "archived",
                "patientId",
            ]:
                continue
            # Check if the key exists in the medical information attributes
            if hasattr(patient.medicalInfo, key):
                setattr(patient.medicalInfo, key, value)

        # Save the updated medical information
        patient.medicalInfo.save()

        # Return the updated medical information in JSON format
        return jsonify(database.get_by_id(MedInfo, patient.medicalInfo.id).to_dict())
    else:
    # Filter out keys that are not attributes of the MedInfo model
        new_data = data.copy()
        for key in data:
            if not hasattr(MedInfo, key):
                new_data.pop(key, None)

        # Create a new MedInfo object with the filtered data and patient ID
        info = MedInfo(**new_data, patientId=str(patientId))

        # Return the newly created medical information in JSON format
        return jsonify(database.get_by_id(MedInfo, str(info.id)).to_dict())
