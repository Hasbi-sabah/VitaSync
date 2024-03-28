import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.vaccine import Vaccine


@api.route('/vaccine/<uuid:vaccineId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_vaccine(vaccineId, current_user):
    """
    Get details of a specific vaccine by its ID.

    Parameters:
    - vaccineId (uuid): The unique identifier of the vaccine.

    Raises:
    - 404: If the vaccine with the provided ID is not found.
    - 403: If the current user does not have sufficient privileges to access the vaccine details.

    Returns:
    - JSON: The vaccine details in JSON format.
    """
    # Retrieve the vaccine from the database using the vaccineId
    vaccine = database.get_by_id(Vaccine, str(vaccineId))
    
    # Check if the vaccine exists
    if not vaccine:
        # Return a 404 error response if the vaccine is not found
        return jsonify({"error": "Vaccine not found"}), 404
    
    # Check if the current user has sufficient privileges to access the vaccine details
    if current_user.role == 'patient':
        if current_user.profileId != vaccine.administeredForId:
            # Return a 403 error response if the user doesn't have sufficient privileges
            return {"error": "Insufficient privileges!"}, 403
    
    # Return the vaccine details in JSON format
    return jsonify(vaccine.to_dict())

@api.route('/vaccine/<uuid:vaccineId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor', 'nurse'])
def update_vaccine(vaccineId, current_user):
    """
    Update details of a specific vaccine by its ID.

    Parameters:
    - vaccineId (uuid): The unique identifier of the vaccine.

    Raises:
    - 404: If the vaccine with the provided ID is not found.
    - 403: If the current user does not have sufficient privileges to update the vaccine details.

    Returns:
    - JSON: The updated vaccine details in JSON format.
    """
    # Get the content type from the request headers
    content_type = request.headers.get('Content-Type')
    
    # Determine the data format based on the content type
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    
    # Retrieve the vaccine from the database using the vaccineId
    vaccine = database.get_by_id(Vaccine, str(vaccineId))
    
    # Check if the vaccine exists
    if not vaccine:
        # Return a 404 error response if the vaccine is not found
        return jsonify({"error": "Vaccine not found"}), 404
    
    # Check if the current user has sufficient privileges to update the vaccine details
    if current_user.role != 'admin':
        if current_user.profileId != vaccine.administeredById:
            # Return a 403 error response if the user doesn't have sufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        
        # Check if the vaccine record can be edited (within 24 hours of creation)
        if vaccine.created_at + (24 * 3600) < time.time():
            # Return a 403 error response if the vaccine record is older than 24 hours
            return {"error": "Can't edit records after 24h"}, 403
    
    # Iterate over the data items and update the vaccine attributes
    for key, value in data.items():
        if current_user.role != 'admin' and key in ['id', 'created_at', 'modified_at', 'archived', 'administeredForId', 'administeredById']:
            continue
        
        # Check if the key is 'drugId' and validate the drug ID
        if key == 'drugId':
            drug = database.get_by_id(Drug, value)
            if not drug:
                # Return a 404 error response if the drug ID is not found
                return jsonify({"error": "Vaccine Drug not found"}), 404
        
        # Set the attribute value if it exists in the vaccine model
        if hasattr(vaccine, key):
            setattr(vaccine, key, value)
    
    # Save the updated vaccine record
    vaccine.save()
    
    # Return the updated vaccine details in JSON format
    return jsonify(database.get_by_id(Vaccine, str(vaccineId)).to_dict())

@api.route('/vaccine/<uuid:vaccineId>', methods=['DELETE'], strict_slashes=False)
@token_required(['doctor', 'nurse'])
def delete_vaccine(vaccineId, current_user):
    """
    Delete a vaccine by its ID.

    Parameters:
    - vaccineId (uuid): The unique identifier of the vaccine.

    Raises:
    - 404: If the vaccine with the provided ID is not found.
    - 403: If the current user does not have sufficient privileges to delete the vaccine.

    Returns:
    - JSON: An empty JSON response indicating successful deletion.
    """
    # Retrieve the vaccine from the database using the vaccineId
    vaccine = database.get_by_id(Vaccine, str(vaccineId))
    
    # Check if the vaccine exists
    if not vaccine:
        # Return a 404 error response if the vaccine is not found
        return jsonify({"error": "Vaccine not found"}), 404
    
    # Check if the current user has sufficient privileges to delete the vaccine
    if current_user.role != 'admin':
        if current_user.profileId != vaccine.administeredById:
            # Return a 403 error response if the user doesn't have sufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        
        # Check if the vaccine record can be edited (within 24 hours of creation)
        if vaccine.created_at + (24 * 3600) < time.time():
            # Return a 403 error response if the vaccine record is older than 24 hours
            return {"error": "Can't edit records after 24h"}, 403
    
    # Archive the vaccine record
    vaccine.archive()
    
    # Return an empty JSON response indicating successful deletion
    return jsonify({})