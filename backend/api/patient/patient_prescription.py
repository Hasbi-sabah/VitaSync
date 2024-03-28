from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.prescription import Prescription

@api.route('/patient/<uuid:patientId>/prescription', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_prescriptions(patientId, current_user):
    """
    Get all prescriptions associated with a patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient.

    Raises:
    - 404: If the patient with the provided ID is not found.
    - 403: If the current user does not have sufficient privileges to access the prescriptions.

    Returns:
    - JSON: A list of dictionaries representing the prescriptions associated with the patient.
    """
    # Retrieve the patient from the database using the patientId
    patient = database.get_by_id(Patient, str(patientId))
    
    # Check if the patient exists
    if not patient:
        # Return a 404 error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404
    
    # Check if the current user has sufficient privileges to access the prescriptions
    if current_user.role == 'patient' and current_user.profileId != str(patientId):
        # Return a 403 error response if the user doesn't have sufficient privileges
        return {"error": "Insufficient privileges!"}, 403
    
    # Filter and jsonify the prescriptions associated with the patient
    return jsonify([prescription.to_dict() for prescription in patient.prescriptions if not prescription.archived])

@api.route('/patient/<uuid:patientId>/prescription', methods=['POST'], strict_slashes=False)
@token_required(['doctor'])
def add_patient_prescription(patientId, current_user):
    """
    Add a new prescription for a patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient.

    Raises:
    - 404: If the patient with the provided ID is not found.

    Returns:
    - JSON: A dictionary representing the newly added prescription.
    """
    # Retrieve the patient from the database using the patientId
    patient = database.get_by_id(Patient, str(patientId))
    
    # Check if the patient exists
    if not patient:
        # Return a 404 error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404
    
    # Get the content type of the request
    content_type = request.headers.get('Content-Type')
    
    # Parse the data based on the content type (JSON or form data)
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    
    # Create a new Prescription object
    prescription = Prescription(notes=data.get('notes', None), prescribedForId=str(patientId), prescribedById=current_user.profileId)
    
    # Return the newly added prescription as JSON
    return jsonify(database.get_by_id(Prescription, str(prescription.id)).to_dict())