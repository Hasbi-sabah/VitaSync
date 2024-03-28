from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.patient import Patient
from models.vaccine import Vaccine

@api.route('/patient/<uuid:patientId>/vaccine', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_vaccines(patientId, current_user):
    """
    Get all vaccines associated with a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient.

    Raises:
    - 404: If the patient with the provided ID is not found.
    - 403: If the user does not have sufficient privileges to access the vaccines.

    Returns:
    - JSON: A list of vaccine objects in JSON format.
    """
    # Retrieve the patient from the database using the patientId
    patient = database.get_by_id(Patient, str(patientId))
    
    # Check if the patient exists
    if not patient:
        # Return a 404 error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404
    
    # Check if the user has sufficient privileges to access the vaccines
    if current_user.role == 'patient' and current_user.profileId != str(patientId):
        # Return a 403 error response if the user does not have sufficient privileges
        return {"error": "Insufficient privileges!"}, 403
    
    # Return a list of vaccine objects associated with the patient
    return jsonify([vaccine.to_dict() for vaccine in patient.vaccines if not vaccine.archived])

@api.route('/patient/<uuid:patientId>/vaccine', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse'])
def add_patient_vaccine(patientId, current_user):
    """
    Add a new vaccine for a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient.

    Raises:
    - 404: If the patient with the provided ID is not found.
    - 400: If the vaccine data is missing or incomplete.
    - 404: If the drug associated with the vaccine is not found.

    Returns:
    - JSON: The newly created vaccine object in JSON format.
    """
    # Retrieve the patient from the database using the patientId
    patient = database.get_by_id(Patient, str(patientId))
    
    # Check if the patient exists
    if not patient:
        # Return a 404 error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404
    
    # Get the content type of the request
    content_type = request.headers.get('Content-Type')
    
    # Extract data from the request based on the content type
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    
    # Check if the required data (drugId) is provided
    if not data.get('drugId', None):
        # Return a 400 error response if the vaccine drug ID is missing
        return jsonify({"error": "Missing vaccine drug ID"}), 400
    
    # Retrieve the drug associated with the vaccine
    drug = database.get_by_id(Drug, str(data.get('drugId')))
    
    # Check if the drug exists
    if not drug:
        # Return a 404 error response if the drug is not found
        return jsonify({"error": "Vaccine Drug not found"}), 404
    
    # Create a new Vaccine object and save it to the database
    vaccine = Vaccine(**data, administeredForId=str(patientId), administeredById=current_user.profileId)
    return jsonify(database.get_by_id(Vaccine, str(vaccine.id)).to_dict())