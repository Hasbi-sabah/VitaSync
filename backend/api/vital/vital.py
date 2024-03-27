import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.vital import Vital


@api.route('/vital/<uuid:vitalId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_vital(vitalId, current_user):
    """
    Retrieves a specific vital take entry by its unique identifier.

    Parameters:
    - vitalId (uuid): The unique identifier of the vital take entry.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response with the vital take entry data in dictionary format.

    Raises:
    - 404: If the vital take entry with the given vitalId is not found in the database.
    - 403: If the current user does not have sufficient privileges to access the vital take entry.
    """
    # Retrieve the vital take entry from the database using the provided vitalId
    vital = database.get_by_id(Vital, str(vitalId))
    if not vital:
        # Return an error response if the vital take entry is not found
        return jsonify({"error": "Vital take not found"}), 404

    # Check if the current user has sufficient privileges to access the vital take entry
    if current_user.role == 'patient' and current_user.profileId != vital.takenForId:
        # Return an error response for insufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    # Return the vital take entry data as a JSON response
    return jsonify(vital.to_dict())

@api.route('/vital/<uuid:vitalId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def update_vital(vitalId, current_user):
    """
    Updates a specific vital take entry identified by its unique identifier.

    Parameters:
    - vitalId (uuid): The unique identifier of the vital take entry to be updated.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response with the updated vital take entry data in dictionary format.
    - Error JSON response if vital take entry is not found, has insufficient privileges, or editing is restricted.

    Raises:
    - 404: If the vital take entry with the given vitalId is not found in the database.
    - 403: If the current user does not have sufficient privileges to update the vital take entry.
    - 403: If the vital take entry was created more than 24 hours ago and cannot be edited.
    """
    # Retrieve the content type of the request
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        # Parse JSON data if the content type is JSON
        data = request.get_json()
    else:
        # Parse form data if the content type is not JSON
        data = request.form.to_dict()

    # Retrieve the vital take entry from the database using the provided vitalId
    vital = database.get_by_id(Vital, str(vitalId))
    if not vital:
        # Return an error response if the vital take entry is not found
        return jsonify({"error": "Vital take not found"}), 404

    # Check if the current user has sufficient privileges to update the vital take entry
    if current_user.role != 'admin':
        if current_user.profileId != vital.takenById:
            # Return an error response for insufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        if vital.created_at + (24 * 3600) < time.time():
            # Return an error response if editing is restricted due to time limitation
            return {"error": "Can't edit records after 24h"}, 403

    # Update the vital take entry attributes based on the provided data
    for key, value in data.items():
        if current_user.role != 'admin' and key in ['id', 'created_at', 'modified_at', 'archived', 'takenById', 'takenForId']:
            continue
        if hasattr(vital, key):
            setattr(vital, key, value)

    # Save the updated vital take entry to the database
    vital.save()

    # Return the updated vital take entry data as a JSON response
    return jsonify(database.get_by_id(Vital, str(vitalId)).to_dict())

@api.route('/vital/<uuid:vitalId>', methods=['DELETE'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def delete_vital(vitalId, current_user):
    """
    Deletes a specific vital sign entry identified by its unique identifier.

    Parameters:
    - vitalId (uuid): The unique identifier of the vital sign entry to be deleted.
    - current_user: The authenticated user making the request.

    Returns:
    - Empty JSON response indicating successful deletion of the vital sign entry.

    Raises:
    - 404: If the vital sign entry with the given vitalId is not found in the database.
    - 403: If the current user does not have sufficient privileges to delete the vital sign entry.
    - 403: If the vital sign entry was created more than 24 hours ago and cannot be deleted.
    """
    # Retrieve the vital sign entry from the database using the provided vitalId
    vital = database.get_by_id(Vital, str(vitalId))
    if not vital:
        # Return an error response if the vital sign entry is not found
        return jsonify({"error": "Vital take not found"}), 404

    # Check if the current user has sufficient privileges to delete the vital sign entry
    if current_user.role != 'admin':
        if current_user.profileId != vital.takenById:
            # Return an error response for insufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        if vital.created_at + (24 * 3600) < time.time():
            # Return an error response if deletion is restricted due to time limitation
            return {"error": "Can't delete records after 24h"}, 403

    # Archive (soft delete) the vital sign entry in the database
    vital.archive()

    # Return an empty JSON response indicating successful deletion
    return jsonify({})