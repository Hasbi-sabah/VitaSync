import secrets
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from api.base import notify
from models.patient import Patient
from models import database
from models.hcw import HCW
from models.user import User


@api.route('/hcw_extended', methods=['GET'] ,strict_slashes=False)
@token_required([])
def get_all_extended_hcws(current_user):
    """
    Get all healthcare workers.

    This endpoint returns a list of healthcare workers with profile and user information.

    Only available for users with admin roles.

    :param current_user: Current authenticated user (obtained from token)
    :return: JSON response with a list of healthcare workers
    """

    # Initialize an empty list to store the response
    res = []

    # Loop through all healthcare workers in the database
    for hcw in database.get_all(HCW):
        
        # Convert the healthcare worker object to a dictionary
        hcw_dict = hcw.to_dict()

        # Get the associated user object for the healthcare worker
        user_dict = database.get_by_id(User, str(hcw.userId)).to_dict()

        # Remove sensitive information from the user dictionary
        user_dict.pop('id', None)  # Remove 'id' field
        user_dict.pop('password', None)  # Remove 'password' field
        user_dict.pop('token', None)  # Remove 'token' field

        # Update the healthcare worker dictionary with user information
        hcw_dict.update(user_dict)

        # Append the extended healthcare worker dictionary to the response list
        res.append(hcw_dict)

    # Return a JSON response with the list of extended healthcare workers
    return jsonify(res)


@api.route('/hcw', methods=['GET'] ,strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_hcws(current_user):
    """
    Get all healthcare workers.

    This endpoint returns a list of healthcare workers.

    Available for all roles.

    :param current_user: Current authenticated user (obtained from token)
    :return: JSON response with a list of healthcare workers
    """

    # Retrieve all healthcare workers from the database and convert them to dictionaries
    res = [hcw.to_dict() for hcw in database.get_all(HCW) if current_user.role == 'admin' or database.get_by_id(User, hcw.userId).role != 'admin']

    # Return a JSON response with the list of healthcare workers
    return jsonify(res)


@api.route('/hcw_extended/<uuid:hcwId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def get_hcw_extended(hcwId, current_user):
    """
    Get extended information about a specific healthcare worker.

    This endpoint retrieves profile and user information about a healthcare worker based on the provided HCW ID.

    Requires a valid token with roles: 'doctor', 'nurse', or 'pharmacist'.
    Admins can access any HCW information, while non-admins can only access their own information.

    :param hcwId: The UUID of the healthcare worker to retrieve information for.
    :type hcwId: str
    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response containing the extended healthcare worker information.
    :rtype: flask.Response
    :raises 404: If the specified healthcare worker ID is not found in the database.
    :raises 403: If the user does not have sufficient privileges to access the information.
    """

    # Retrieve the healthcare worker object from the database based on the provided ID
    hcw = database.get_by_id(HCW, str(hcwId))

    # Check if the healthcare worker exists
    if not hcw:
        return jsonify({"error": "Health Care Worker not found!"}), 404

    # Check if the current user has sufficient privileges to access the information
    if current_user.role != 'admin' and current_user.profileId != str(hcwId):
        return {"error": "Insufficient privileges!"}, 403

    # Convert the healthcare worker object to a dictionary
    hcw_dict = hcw.to_dict()

    # Get the associated user object for the healthcare worker and convert it to a dictionary
    user_dict = database.get_by_id(User, str(hcw.userId)).to_dict()

    # Remove sensitive information from the user data (optional)
    user_dict.pop('id', None)
    user_dict.pop('password', None)

    # Merge the user data into the healthcare worker data
    hcw_dict.update(user_dict)

    # Return a JSON response containing the extended healthcare worker information
    return jsonify(hcw_dict)


@api.route('/hcw/<uuid:hcwId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_hcw(hcwId, current_user):
    """
    Get detailed information about a specific healthcare worker.

    This endpoint retrieves detailed information about a healthcare worker based on the provided HCW ID.

    Requires a valid token with roles: 'doctor', 'nurse', or 'pharmacist'.
    Admins can access any HCW information, while non-admins can only access their own information.

    :param hcwId: The UUID of the healthcare worker to retrieve information for.
    :type hcwId: str
    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response containing the detailed healthcare worker information.
    :rtype: flask.Response
    :raises 404: If the specified healthcare worker ID is not found in the database.
    :raises 403: If the user does not have sufficient privileges to access the information.
    """

    # Retrieve the healthcare worker object from the database based on the provided ID
    hcw = database.get_by_id(HCW, str(hcwId))

    # Check if the healthcare worker exists
    if not hcw:
        return jsonify({"error": "Health Care Worker not found!"}), 404

    # Check if the current user has sufficient privileges to access the information
    if current_user.role != 'admin' and current_user.profileId != str(hcwId):
        return {"error": "Insufficient privileges!"}, 403

    # Return a JSON response containing the detailed healthcare worker information
    return jsonify(hcw.to_dict())


@api.route('/hcw', methods=['POST'], strict_slashes=False)
@token_required([])
def add_hcw(current_user):
    """
    Add a new healthcare worker.

    This endpoint allows administrators to add a new healthcare worker to the system.
    The request should include the following required attributes in JSON format or form data:
    - firstName: First name of the healthcare worker.
    - lastName: Last name of the healthcare worker.
    - CIN: Identity card number of the healthcare worker.
    - licence: Medical licence number of the healthcare worker.
    - speciality: Speciality or field of expertise of the healthcare worker.
    - workAddress: Work address of the healthcare worker.
    - workNumber: Work contact number of the healthcare worker.
    - role: Role or position of the healthcare worker.
    - email: Email address of the healthcare worker.

    Optional attributes that can be provided:
    - password: Password for the healthcare worker (if not provided, a random password will be generated).
    - username: Username for the healthcare worker (if not provided, it will be derived from the email address).

    Returns a JSON response with the newly added healthcare worker's information if successful.

    :param current_user: Current authenticated user (obtained from token).
    :return: JSON response with the newly added healthcare worker's information or an error message.
    :raises 400: If any of the required attributes are missing in the request.
    :raises 404: If the specified healthcare worker ID is not found in the database.
    :raises 403: If the user does not have sufficient privileges to access the information.
    :raises 409: If the licence number or email address already exists in the database.
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Check for required attributes
    for attr in ['firstName', 'lastName', 'CIN', 'licence', 'speciality', 'workAddress', 'workNumber', 'role', 'email']:
        val = data.get(attr, None)
        if not val:
            return jsonify({"error": f"Missing {attr}"}), 400

    # Check if the CIN already exists in the database
    if database.search(HCW, CIN=data.get('CIN', None)) or database.search(Patient, CIN=data.get('CIN', None)):
        return jsonify({"error": "CIN already exists in database"}), 409

    # Check if the licence number already exists in the database
    if database.search(HCW, licence=data.get('licence', None)):
        return jsonify({"error": "License already exists in database"}), 409

    # Check if the email address already exists in the database
    if database.search(User, email=data.get('email', None)):
        return jsonify({"error": "Email already exists in database"}), 409
    
    # Generate a random password if not provided
    if not data.get('password', None):
        data['password'] = secrets.token_urlsafe(10)

    # Generate username from email address if not provided
    if not data.get('username', None):
        username = data.get('email').split('@')[0]
        if database.search(User, username=username):
            return jsonify({"error": "Could not generate username, please include it in the next request"}), 400
        data['username'] = username

    new_data = data.copy()
    for key in data:
        if not hasattr(HCW, key) and not hasattr(User, key):
            new_data.pop(key, None)

    # Create and add the new healthcare worker to the database
    hcw = HCW(**new_data)
    
    # Notify the user about their credentials by email
    notify(hcw.userId, 1, name=f'{hcw.lastName} {hcw.firstName}', username=database.get_by_id(User, str(hcw.userId)).username, password=new_data['password'])
    
    # Return a JSON response with the newly added healthcare worker's information
    return jsonify(database.get_by_id(HCW, str(hcw.id)).to_dict())


@api.route('/hcw/<uuid:hcwId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist'])
def update_hcw(hcwId, current_user):
    """
    Update a healthcare worker's information.

    This endpoint allows authorized users (doctors, nurses, pharmacists) to update a healthcare worker's information
    in the system. The request should include the healthcare worker's ID in the URL path (<uuid:hcwId>) and provide
    the updated attributes in JSON format or form data.

    Attributes to update:
    - firstName: Updated first name of the healthcare worker.
    - lastName: Updated last name of the healthcare worker.
    - CIN: Updated identity card number of the healthcare worker.
    - licence: Updated medical licence number of the healthcare worker.
    - speciality: Updated speciality or field of expertise of the healthcare worker.
    - workAddress: Updated work address of the healthcare worker.
    - workNumber: Updated work contact number of the healthcare worker.
    - email: Updated email of the healthcare worker. (needs to be unique)
    - username: Updated username of the healthcare worker. (needs to be unique)

    Returns a JSON response with the updated healthcare worker's information if successful.

    :param hcwId: ID of the healthcare worker to update (obtained from URL).
    :param current_user: Current authenticated user (obtained from token).
    :return: JSON response with the updated healthcare worker's information or an error message.
    :raises 404: If the specified healthcare worker ID is not found in the database.
    :raises 403: If the user does not have sufficient privileges to access the information.
    :raises 400: If attribute already exists.
    """

    # Check content type and get data
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Get the healthcare worker from the database
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404

    # Get the user object associated with the patient
    user = database.get_by_id(User, hcw.userId)
    
    # Check permissions
    if current_user.role != 'admin' and current_user.profileId != str(hcwId):
        return jsonify({"error": "Insufficient privileges!"}), 403

    # Iterate over the key-value pairs in the data dictionary
    for key, value in data.items():
        # Check if the current user is not an admin and the key is in the restricted list
        if current_user.role != 'admin' and key in ['id', 'created_at', 'modified_at', 'archived', 'profileId', 'role', 'userId', 'password', 'token']:
            continue  # Skip processing for restricted attributes
        
        # Check for specific attributes and if they already exist in the database
        for attr in ['username', 'email']:
            if key == attr and database.search(User, **{key: value}):
                # Return a 409 Conflict error if the attribute already exists in the database
                return jsonify({"error": f"{attr} already exists in database"}), 409
     
        # Check for specific attributes and if they already exist in the database
        for attr in ['CIN', 'licence']:
            if key == attr and (database.search(HCW, **{key: value}) or database.search(Patient, **{key: value})):
                # Return a 409 Conflict error if the attribute already exists in the database
                return jsonify({"error": f"{attr} already exists in database"}), 409   
        
        # Check if the attribute exists in the HCW model, and update if so
        if hasattr(hcw, key):
            setattr(hcw, key, value)
        # If the attribute doesn't exist in the HCW model, check if it exists in the current user model, and update if so
        elif hasattr(user, key):
            setattr(user, key, value)

    # Save the changes to the database
    hcw.save()
    current_user.save()
    
    # Return the updated healthcare worker's information
    return jsonify(database.get_by_id(HCW, str(hcwId)).to_dict())


@api.route('/hcw/<uuid:hcwId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_hcw(hcwId, current_user):
    """
    Delete (archive) a healthcare worker.

    This endpoint allows administrators to delete (archive) a healthcare worker from the system.
    The request should include the healthcare worker's ID in the URL path (<uuid:hcwId>).

    Returns an empty JSON response if the deletion is successful.

    :param hcwId: ID of the healthcare worker to delete (obtained from URL).
    :param current_user: Current authenticated user (obtained from token).
    :return: Empty JSON response if successful deletion, or an error message.
    :raises 404: If the specified healthcare worker ID is not found in the database.
    """
    # Get the healthcare worker from the database
    hcw = database.get_by_id(HCW, str(hcwId))
    if not hcw:
        return jsonify({"error": "Health Care Worker not found"}), 404

    # Get the associated user and archive both
    user = database.get_by_id(User, hcw.userId)
    hcw.archive()
    user.archive()

    # Return an empty JSON response to indicate successful deletion
    return jsonify({})
