from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.vital import Vital

@api.route('/patient/<uuid:patientId>/vital', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_patient_vitals(patientId, current_user):
    """
    Get all vital signs of a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient whose vitals are to be retrieved.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response with a list of vital signs in dictionary format on success.
    - JSON response with error message and status code:
    
    Raises:
    - 404 Not Found if the patient is not found.
    - 403 Forbidden if the current user has insufficient privileges.
    """
     # Get the patient object from the database based on the patientId
    patient = database.get_by_id(Patient, str(patientId))
    
    # Check if the patient exists in the database
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    # Check if the current user has sufficient privileges to access the patient's vitals
    if current_user.role == 'patient' and current_user.profileId != str(patientId):
        return {"error": "Insufficient privileges!"}, 403

    # Return the list of vital signs associated with the patient from the database
    return jsonify([vital.to_dict() for vital in database.search(Vital, takenForId=str(patientId))])

@api.route('/patient/<uuid:patientId>/vital', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def add_patient_vital(patientId, current_user):
    """
    Adds a new vital take entry for a specific patient.

    Parameters:
    - patientId (uuid): The unique identifier of the patient.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response with the newly added vital sign entry in dictionary format.
    
    Raises:
    - 404 Not Found if the patient is not found.
    """
    # Retrieve the patient from the database using the provided patientId
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        # Return an error response if the patient is not found
        return jsonify({"error": "Patient not found"}), 404

    # Determine the content type of the request
    content_type = request.headers.get('Content-Type')

    # Parse data based on the content type
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Filter out keys that do not belong to the Vital model
    new_data = data.copy()
    for key in data:
        if not hasattr(Vital, key):
            new_data.pop(key, None)

    # Create a new Vital instance with the filtered data
    vital = Vital(**new_data, takenForId=patientId, takenById=current_user.profileId)

    # Return the newly added vital sign entry as a JSON response
    return jsonify(database.get_by_id(Vital, str(vital.id)).to_dict())