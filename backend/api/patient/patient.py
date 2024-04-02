import secrets
import time
from flask import jsonify, request
from api import api
from api.base import input_to_timestamp, notify
from models.hcw import HCW
from models import database
from models.patient import Patient
from models.user import User
from api.auth_middleware import token_required


@api.route("/patient_extended", methods=["GET"], strict_slashes=False)
@token_required([])
def get_all_extended_patients(current_user):
    """
    Get extended details of all patients.

    Parameters:
    - current_user (User): The user making the request (only admin has access to this endpoint).

    Returns:
    - JSON object containing extended details of all patients.
    """
    # Initialize an empty list to store extended patient details
    res = []

    # Iterate over all patients in the database
    for patient in database.get_all(Patient):
        # Convert patient object to a dictionary
        patient_dict = patient.to_dict()

        # Retrieve user details of the patient using the patient's user ID
        user_dict = database.get_by_id(User, str(patient.userId)).to_dict()

        # Remove sensitive information from the user dictionary
        user_dict.pop("id", None)  # Remove user ID
        user_dict.pop("password", None)  # Remove password
        user_dict.pop("token", None)  # Remove authentication token

        # Merge patient and user dictionaries to create an extended patient dictionary
        patient_dict.update(user_dict)

        # Append the extended patient dictionary to the result list
        res.append(patient_dict)

    # Return the result list containing extended patient details in JSON format
    return jsonify(res)


@api.route("/search_patient", methods=["POST"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def list_patients(current_user):
    """
    Get details of all patients.

    Parameters:
    - current_user (User): The user making the request (doctor, nurse, or pharmacist with token-based authentication).

    Returns:
    - JSON object containing details of all patients.
    """
    content_type = request.headers.get("Content-Type")

    # Parse the request data based on content type
    if content_type == "application/json":
        data = request.get_json()
    else:
        ids = request.args.get('ids', None)
        if ids:
            data = {'ids': ids.split(',')}
        else:
            data = None
    print(data)
    if data and data.get('ids', None) != None:
        patients_list = []
        ids = data.get('ids', None)
        for id in ids:
            patient = database.get_by_id(Patient, id)
            if patient:
                patients_list.append(patient)
    else:
    # Retrieve all patients from the database and convert each patient object to a dictionary
        patients_list = database.get_all(Patient)

    # Return the list of patient dictionaries as a JSON response
    return jsonify([patient.to_dict() for patient in patients_list])

@api.route("/patient", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def get_all_patients(current_user):
    """
    Get all healthcare workers.

    This endpoint returns a list of healthcare workers.

    Available for all roles.

    :param current_user: Current authenticated user (obtained from token)
    :return: JSON response with a list of healthcare workers
    """

    # Retrieve all healthcare workers from the database and convert them to dictionaries
    res = [
        patient.to_dict()
        for patient in database.get_all(Patient)
    ]

    # Return a JSON response with the list of healthcare workers
    return jsonify(res)

@api.route("/patient/<uuid:patientId>", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_patient(patientId, current_user):
    """
    Get details of a specific patient identified by patientId.

    Parameters:
    - patientId (str): Unique identifier of the patient to retrieve details for.
    - current_user (User): The user making the request with token-based authentication.

    Returns:
    - JSON object containing the details of the requested patient.

    Raises:
    - 404 Not Found: If the patient with the specified ID is not found.
    - 403 Forbidden: If the current user does not have sufficient privileges to access the patient's details.
    """
    # Retrieve the patient from the database based on the provided patientId
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        # Return a 404 Not Found error if the patient is not found in the database
        return jsonify({"error": "Patient not found"}), 404

    # Check if the current user has the 'patient' role
    if current_user.role == "patient":
        # Check if the current user is trying to access their own profile
        if current_user.profileId != str(patientId):
            # Return a 403 Forbidden error if the user does not have sufficient privileges
            return jsonify({"error": "Insufficient privileges!"}), 403

    # Return the details of the patient in JSON format
    return jsonify(patient.to_dict())


@api.route("/patient_extended/<uuid:patientId>", methods=["GET"], strict_slashes=False)
@token_required(["patient"])
def get_patient_extended(patientId, current_user):
    """
    Get extended details of a specific patient identified by patientId.

    Parameters:
    - patientId (UUID): Unique identifier of the patient to retrieve extended details for.
    - current_user (User): The user making the request with token-based authentication (patient role required).

    Returns:
    - JSON object containing extended details of the requested patient.

    Raises:
    - 404 Not Found: If the patient with the specified ID is not found.
    - 403 Forbidden: If the current user does not have sufficient privileges to access the patient's extended details.
    """
    # Retrieve the patient from the database based on the provided patientId
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        # Return a 404 Not Found error if the patient is not found in the database
        return jsonify({"error": "Patient not found"}), 404

    # Check if the current user is a patient and trying to access their own profile
    if current_user.role == "patient" and current_user.profileId != str(patientId):
        # Return a 403 Forbidden error if the user does not have sufficient privileges
        return jsonify({"error": "Insufficient privileges!"}), 403

    # Convert patient object to a dictionary
    patient_dict = patient.to_dict()

    # Retrieve user details of the patient using the patient's user ID
    user_dict = database.get_by_id(User, str(patient.userId)).to_dict()

    # Remove sensitive information from the user dictionary
    user_dict.pop("id", None)  # Remove user ID
    user_dict.pop("password", None)  # Remove password
    user_dict.pop("token", None)  # Remove authentication token

    # Merge patient and user dictionaries to create an extended patient dictionary
    patient_dict.update(user_dict)

    # Return the extended details of the patient in JSON format
    return jsonify(patient_dict)


@api.route("/patient", methods=["POST"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def add_patient(current_user):
    """
    Add a new patient to the system.

    This function handles the creation of a new patient record based on the provided data.
    It validates the required attributes and checks for existing usernames or emails in the database.

    Parameters:
    - current_user (User): The user making the request with token-based authentication.

    Returns:
    - JSON object containing the details of the newly added patient.

    Raises:
    - 400 Bad Request: If any required attribute is missing or if there's an issue generating the username.
    - 409 Conflict: If the provided username or email already exists in the database.
    """
    # Get the content type from the request headers
    content_type = request.headers.get("Content-Type")

    # Parse the request data based on the content type (JSON or form data)
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Validate required attributes for creating a new patient
    for attr in [
        "firstName",
        "lastName",
        "CIN",
        "sex",
        "phoneNumber",
        "address",
        "birthDate",
        "email",
    ]:
        if not data.get(attr, None):
            return jsonify({"error": f"Missing {attr}"}), 400

    # Check if username or email or CIN already exists in the database
    if database.search(HCW, CIN=data.get("CIN", None)) or database.search(
        Patient, CIN=data.get("CIN", None)
    ):
        return jsonify({"error": "CIN already exists in database"}), 409
    if data.get("username", None) and database.search(
        User, username=data.get("username")
    ):
        return jsonify({"error": "Username already exists in database"}), 409
    if database.search(User, email=data.get("email", None)):
        return jsonify({"error": "Email already exists in database"}), 409

    # Generate a random password if not provided
    if not data.get("password", None):
        data["password"] = secrets.token_urlsafe(10)

    # Generate username if not provided and check for its existence in the database
    if not data.get("username", None):
        username = data.get("email").split("@")[0]
        if database.search(User, username=username):
            return (
                jsonify(
                    {
                        "error": "Could not generate username, please include it in the next request"
                    }
                ),
                400,
            )
        data["username"] = username

    # Convert the birthdate input to a timestamp using the input_to_timestamp function
    timestamp = input_to_timestamp(data.get("birthDate"), "%Y-%m-%d")

    # Check if the timestamp conversion was successful
    if not timestamp:
        # Return a 400 Bad Request response with an error message for invalid input format
        return jsonify({"error": "Invalid input format. Ex: 2024-04-01"}), 400

    # Check if the birthdate timestamp is in the future
    if timestamp > time.time():
        # Return a 400 Bad Request response with an error message indicating birthdate can't be in the future
        return jsonify({"error": "BirthDate can't be in the future"}), 400

    # Update the birthDate field in the data dictionary with the validated timestamp
    data["birthDate"] = timestamp

    new_data = data.copy()
    for key in data:
        if not hasattr(Patient, key) and not hasattr(User, key):
            new_data.pop(key, None)

    # Create a new patient object using the provided data
    patient = Patient(**new_data)

    user = database.get_by_id(User, objId=patient.userId)

    # Send email notification to the patient with credentials
    notify(
        patient.userId,
        1,
        name=f"{patient.lastName} {patient.firstName}",
        username=user.username,
        password=data["password"],
    )

    # Save the newly created patient to the database and return its details
    return jsonify(database.get_by_id(Patient, str(patient.id)).to_dict())


@api.route("/patient/<uuid:patientId>", methods=["PUT"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist"])
def update_patient(patientId, current_user):
    """
    Update patient details in the system.

    Parameters:
    - patientId (uuid): The unique identifier of the patient to be updated.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response with updated patient details on success.
    - JSON response with appropriate error message and status code on failure:

    Raises:
    - 404 Not Found if the patient is not found.
    - 400 Bad Request if there's an invalid input format or birthDate in the future.
    - 409 Conflict if a CIN, username, or email already exists in the database.
    """

    # Get the content type from the request headers
    content_type = request.headers.get("Content-Type")

    # Parse the request data based on the content type (JSON or form data)
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Get the patient object from the database based on the patientId
    patient = database.get_by_id(Patient, str(patientId))

    # Check if the patient exists
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    # Get the user object associated with the patient
    user = database.get_by_id(User, patient.userId)

    # Iterate through the data items and update patient and user attributes
    for key, value in data.items():
        # Check if the current user is not an admin and the key is in the restricted list
        if current_user.role != "admin" and key in [
            "id",
            "created_at",
            "modified_at",
            "archived",
            "profileId",
            "role",
            "userId",
            "password",
            "token",
        ]:
            continue

        # Check for specific attributes (username, email) and if they already exist in the database
        for attr in ["username", "email"]:
            if key == attr and database.search(User, **{key: value}):
                return jsonify({"error": f"{attr} already exists in database"}), 409

        if key == "CIN" and (
            database.search(HCW, CIN=data.get("CIN", None))
            or database.search(Patient, CIN=data.get("CIN", None))
        ):
            return jsonify({"error": f"{key} already exists in database"}), 409

        # Convert birthDate to timestamp format and validate it
        if key == "birthDate" and value:
            timestamp = input_to_timestamp(value, "%Y-%m-%d")
            if not timestamp:
                return jsonify({"error": "Invalid input format. Ex: 2024-04-01"}), 400
            if timestamp > time.time():
                return jsonify({"error": "BirthDate can't be in the future"}), 400
            value = timestamp

        # Update patient attributes if the key exists in the Patient model
        if hasattr(patient, key):
            setattr(patient, key, value)
        # Update user attributes if the key exists in the User model
        elif hasattr(user, key):
            setattr(user, key, value)

    # Save the updated patient and user objects
    patient.save()
    user.save()

    # Return the updated patient details in JSON format
    return jsonify(database.get_by_id(Patient, str(patientId)).to_dict())


@api.route("/patient/<uuid:patientId>", methods=["DELETE"], strict_slashes=False)
@token_required([])
def delete_patient(patientId, current_user):
    """
    Delete a patient and associated user from the system.

    Parameters:
    - patientId (uuid): The unique identifier of the patient to be deleted.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response with empty data on successful deletion.
    - JSON response with error message and status code:

    Raises:
    - 404 Not Found if the patient is not found.
    """

    # Get the patient object from the database based on the patientId
    patient = database.get_by_id(Patient, str(patientId))

    # Check if the patient exists
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    # Get the user object associated with the patient
    user = database.get_by_id(User, patient.userId)

    # Archive the patient and user objects (soft delete)
    patient.archive()
    user.archive()
    for appt in patient.appointments:
        appt.archive()

    # Return an empty JSON response to indicate successful deletion
    return jsonify({})
