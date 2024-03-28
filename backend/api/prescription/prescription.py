import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.prescription import Prescription


@api.route('/prescription/<uuid:prescriptionId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_prescription(prescriptionId, current_user):
    """
    Get details of a specific prescription.

    Parameters:
    - prescriptionId (uuid): The unique identifier of the prescription.

    Raises:
    - 404: If the prescription with the provided ID is not found.

    Returns:
    - JSON: A dictionary representing the prescription details.
    """
    # Retrieve the prescription from the database using the prescriptionId
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    
    # Check if the prescription exists
    if not prescription:
        # Return a 404 error response if the prescription is not found
        return jsonify({"error": "Prescription not found"}), 404
    
    # Check user role and profile ID for permissions
    if current_user.role == 'patient' and current_user.profileId != prescription.prescribedForId:
        # Return a 403 error response for insufficient privileges
        return {"error": "Insufficient privileges!"}, 403
    
    # Return the prescription details as JSON
    return jsonify(prescription.to_dict())

@api.route('/prescription/<uuid:prescriptionId>/fill', methods=['POST'], strict_slashes=False)
@token_required(['pharmacist'])
def prescription_fill(prescriptionId, current_user):
    """
    Fill a prescription with the given prescriptionId.

    Parameters:
    - prescriptionId (uuid): The unique identifier of the prescription to fill.

    Raises:
    - 404: If the prescription with the provided ID is not found.
    - 409: If the prescription is already filled.

    Returns:
    - JSON: A dictionary representing the filled prescription details.
    """
    # Retrieve the prescription from the database using the prescriptionId
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    
    # Check if the prescription exists
    if not prescription:
        # Return a 404 error response if the prescription is not found
        return jsonify({"error": "Prescription not found"}), 404
    
    # Check if the prescription is already filled
    if prescription.status:
        # Return a 409 error response if the prescription is already filled
        return jsonify({"error": "Prescription already filled"}), 409
    
    # Update the prescription status and filledById
    setattr(prescription, 'status', True)
    setattr(prescription, 'filledById', current_user.profileId)
    
    # Save the changes to the prescription
    prescription.save()
    
    # Return the filled prescription details as JSON
    return jsonify(prescription.to_dict())

@api.route('/prescription/<uuid:prescriptionId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_prescription(prescriptionId, current_user):
    """
    Update a prescription with the given prescriptionId.

    Parameters:
    - prescriptionId (uuid): The unique identifier of the prescription to update.

    Raises:
    - 404: If the prescription with the provided ID is not found.
    - 403: If the user has insufficient privileges or tries to edit a filled prescription.

    Returns:
    - JSON: A dictionary representing the updated prescription details.
    """
    # Get the content type from the request headers
    content_type = request.headers.get('Content-Type')
    
    # Check if the content type is JSON or form data
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    
    # Retrieve the prescription from the database using the prescriptionId
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    
    # Check if the prescription exists
    if not prescription:
        # Return a 404 error response if the prescription is not found
        return jsonify({"error": "Prescription not found"}), 404
    
    # Check user privileges and prescription status before allowing update
    if current_user.role != 'admin':
        if current_user.profileId != prescription.prescribedById:
            # Return a 403 error response if the user has insufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        
        if prescription.status:
            # Return a 403 error response if trying to edit a filled prescription
            return {"error": "Can't edit a filled prescription!"}, 403
    
    # Update prescription attributes based on user input
    for key, value in data.items():
        if key == 'notes' or current_user.role == 'admin':
            setattr(prescription, key, value)
    
    # Save the updated prescription
    prescription.save()
    
    # Return the updated prescription details as JSON
    return jsonify(database.get_by_id(Prescription, str(prescriptionId)).to_dict())

@api.route('/prescription/<uuid:prescriptionId>', methods=['DELETE'], strict_slashes=False)
@token_required(['doctor'])
def delete_prescription(prescriptionId, current_user):
    """
    Delete a prescription with the given prescriptionId.

    Parameters:
    - prescriptionId (uuid): The unique identifier of the prescription to delete.

    Raises:
    - 404: If the prescription with the provided ID is not found.
    - 403: If the user has insufficient privileges or tries to delete a prescription after 24 hours of creation.

    Returns:
    - JSON: An empty response if the prescription is successfully deleted.
    """
    # Retrieve the prescription from the database using the prescriptionId
    prescription = database.get_by_id(Prescription, str(prescriptionId))
    
    # Check if the prescription exists
    if not prescription:
        # Return a 404 error response if the prescription is not found
        return jsonify({"error": "Prescription not found"}), 404
    
    # Check user privileges and prescription creation time before allowing deletion
    if current_user.role != 'admin':
        if current_user.profileId != prescription.prescribedById:
            # Return a 403 error response if the user has insufficient privileges
            return {"error": "Insufficient privileges!"}, 403
        
        if prescription.created_at + (24 * 3600) < time.time():
            # Return a 403 error response if trying to delete a prescription after 24 hours of creation
            return {"error": "Can't delete records after 24h"}, 403
    
    # Archive the prescription (soft delete)
    prescription.archive()
    
    # Return an empty JSON response indicating successful deletion
    return jsonify({})