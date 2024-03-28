import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.med_info import MedInfo


@api.route("/med_info/<uuid:infoId>", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_med_info(infoId, current_user):
    """
    Retrieve medical information by ID.

    Args:
        infoId (uuid): The UUID of the medical information to retrieve.
        current_user: The user making the request (doctor, nurse, pharmacist, or patient).

    Returns:
        JSON: A JSON response containing the requested medical information.

    Raises:
        404: If the medical information with the provided ID is not found.
        403: If the requesting user has insufficient privileges.

    Note:
        This endpoint is accessible to doctors, nurses, pharmacists, and patients with valid tokens.
    """
    # Retrieve the medical information from the database
    med_info = database.get_by_id(MedInfo, str(infoId))

    # Check if the medical information exists
    if not med_info:
        return jsonify({"error": "Medical Info not found"}), 404

    # Check if the requesting user has permission to access the medical information
    if current_user.role == "patient" and current_user.profileId != med_info.patientId:
        return {"error": "Insufficient privileges!"}, 403

    # Return the medical information in JSON format
    return jsonify(med_info.to_dict())


@api.route("/med_info/<uuid:infoId>", methods=["PUT"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def update_med_info(infoId, current_user):
    """
    Update medical information by ID.

    Args:
        infoId (uuid): The UUID of the medical information to update.
        current_user: The user making the request (doctor, nurse, pharmacist).

    Returns:
        JSON: A JSON response containing the updated medical information.

    Raises:
        404: If the medical information with the provided ID is not found.

    Note:
        This endpoint is accessible to doctors, nurses, and pharmacists with valid tokens.
        The 'admin' role can modify all fields, while other roles are restricted from modifying certain fields.
    """
    # Retrieve the content type of the request
    content_type = request.headers.get("Content-Type")

    # Check if the request content type is JSON
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Retrieve the medical information from the database
    med_info = database.get_by_id(MedInfo, str(infoId))

    # Check if the medical information exists
    if not med_info:
        return jsonify({"error": "Medical Info not found"}), 404

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
        if hasattr(med_info, key):
            setattr(med_info, key, value)

    # Save the updated medical information
    med_info.save()

    # Return the updated medical information in JSON format
    return jsonify(database.get_by_id(MedInfo, str(infoId)).to_dict())


@api.route("/med_info/<uuid:infoId>", methods=["DELETE"], strict_slashes=False)
@token_required([])
def delete_med_info(infoId, current_user):
    """
    Delete medical information by ID.

    Args:
        infoId (uuid): The UUID of the medical information to delete.
        current_user: The user making the request.

    Returns:
        JSON: An empty JSON response indicating successful deletion.

    Raises:
        404: If the medical information with the provided ID is not found.
    """
    # Retrieve the medical information from the database
    med_info = database.get_by_id(MedInfo, str(infoId))

    # Check if the medical information exists
    if not med_info:
        return jsonify({"error": "Medical Info not found"}), 404

    # Archive the medical information
    med_info.archive()

    # Remove the medical information reference from the patient
    med_info.patient.medicalInfo = None

    # Return an empty JSON response to indicate successful deletion
    return jsonify({})
