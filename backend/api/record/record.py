import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.record import Record


@api.route("/record/<uuid:recordId>", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient", "admin"])
def get_record(recordId, current_user):
    """
    Get a record by ID.

    Args:
        recordId (uuid): The UUID of the record to retrieve.
        current_user: The user making the request.

    Returns:
        JSON: The record information in JSON format.

    Raises:
        404: If the record with the provided ID is not found.
        403: If the user has insufficient privileges to access the record.
    """
    # Retrieve the record from the database
    record = database.get_by_id(Record, str(recordId))

    # Check if the record exists
    if not record:
        return jsonify({"error": "Record not found"}), 404

    # Check user privileges for patient role
    if current_user.role == "patient":
        if current_user.profileId != record.patientId:
            return {"error": "Insufficient privileges!"}, 403

    # Return the record information in JSON format
    return jsonify(record.to_dict())


@api.route("/record/<uuid:recordId>", methods=["PUT"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def update_record(recordId, current_user):
    """
    Update a record by ID.

    Args:
        recordId (uuid): The UUID of the record to update.
        current_user: The user making the request.

    Returns:
        JSON: The updated record information in JSON format.

    Raises:
        404: If the record with the provided ID is not found.
        403: If the user has insufficient privileges to update the record or if trying to edit a record after 24h.
    """
    # Get the content type of the request
    content_type = request.headers.get("Content-Type")

    # Determine the data format based on content type
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Retrieve the record from the database
    record = database.get_by_id(Record, str(recordId))

    # Check if the record exists
    if not record:
        return jsonify({"error": "Record not found"}), 404

    # Check user privileges and time limit for editing records
    if current_user.role != "admin":
        if current_user.profileId != record.assessedById:
            return {"error": "Insufficient privileges!"}, 403
        if record.created_at + (24 * 3600) < time.time():
            return {"error": "Can't edit records after 24h"}, 403

    # Update the record attributes based on user input
    for key, value in data.items():
        if key in ["diagnosis", "notes"] or current_user.role == "admin":
            setattr(record, key, value)

    # Save the updated record
    record.save()

    # Return the updated record information in JSON format
    return jsonify(database.get_by_id(Record, str(recordId)).to_dict())


@api.route("/record/<uuid:recordId>", methods=["DELETE"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def delete_record(recordId, current_user):
    """
    Delete a record by ID.

    Args:
        recordId (uuid): The UUID of the record to delete.
        current_user: The user making the request.

    Returns:
        JSON: An empty JSON response indicating successful deletion.

    Raises:
        404: If the record with the provided ID is not found.
        403: If the user has insufficient privileges to delete the record or if trying to delete a record after 24h.
    """
    # Retrieve the record from the database
    record = database.get_by_id(Record, str(recordId))

    # Check if the record exists
    if not record:
        return jsonify({"error": "Record not found"}), 404

    # Check user privileges and time limit for deleting records
    if current_user.role != "admin":
        if current_user.profileId != record.assessedById:
            return {"error": "Insufficient privileges!"}, 403
        if record.created_at + (24 * 3600) < time.time():
            return {"error": "Can't delete records after 24h"}, 403

    # Archive the record to mark it as deleted
    record.archive()

    # Return an empty JSON response indicating successful deletion
    return jsonify({})
