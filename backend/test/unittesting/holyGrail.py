from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.hcw import HCW
from models.user import User
from api.base import notify, input_to_timestamp

# Drug Endpoints

@api.route("/drug", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_drugs(current_user):
    """
    Get all drugs or filter drugs based on provided criteria.

    Parameters:
    - current_user (User): The user making the request, with token-based authentication.

    Query Parameters:
    - Query parameters are optional and can be used to filter the drugs.
    - Valid query parameters correspond to attributes of the Drug model.

    Returns:
    - JSON object containing a list of drugs that match the query parameters, or all drugs if no parameters are provided.
    """
    # Check the content type of the request
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Process query parameters for filtering
    if data:
        new_data = data.copy()
        for key in data:
            # Check if the query parameter corresponds to a valid attribute of the Drug model
            if not hasattr(Drug, key):
                new_data.pop(key)  # Remove invalid query parameters
        # Search for drugs in the database based on the filtered criteria
        res = [drug.to_dict() for drug in database.search(Drug, **new_data)]
    else:
        # If no query parameters are provided, fetch all drugs from the database
        res = [drug.to_dict() for drug in database.get_all(Drug)]

    # Return the list of drugs in JSON format
    return jsonify(res)


@api.route("/drug_lookup", methods=["POST"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def drug_lookup(current_user):
    """
    Lookup drugs based on name.

    Parameters:
    - current_user (User): The user making the request, with token-based authentication.

    Query Parameters:
    - name (str, optional): The name of the drug to lookup.

    Returns:
    - JSON object containing a list of drugs that match the lookup criteria.
    """
    # Check the content type of the request
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Perform drug lookup based on the provided name (if any)
    res = [drug.to_dict() for drug in database.drug_lookup(name=data.get("name", ""))]

    # Return the list of drugs in JSON format
    return jsonify(res)


@api.route("/drug/<uuid:drugId>", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_drug(drugId, current_user):
    """
    Get details of a specific drug identified by drugId.

    Parameters:
    - drugId (UUID): Unique identifier of the drug to retrieve details for.
    - current_user (User): The user making the request, with token-based authentication.

    Returns:
    - JSON object containing the details of the requested drug.

    Raises:
    - 404 Not Found: If the drug with the specified ID is not found.
    """
    # Retrieve the drug from the database based on the provided drugId
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        # Return a 404 Not Found error if the drug is not found in the database
        return jsonify({"error": "Drug not found"}), 404

    # Return the details of the drug in JSON format
    return jsonify(drug.to_dict())


@api.route("/drug", methods=["POST"], strict_slashes=False)
@token_required(["pharmacist"])
def add_drug(current_user):
    """
    Add a new drug to the database.

    Parameters:
    - current_user (User): The user making the request, with token-based authentication (pharmacist role required).

    Request Body Attributes:
    - commercialName (str): The commercial name of the drug.
    - activeIngredient (str): The active ingredient(s) of the drug.
    - distributor (str): The distributor or supplier of the drug.
    - dose (str): The dosage information for the drug.
    - form (str): The form of the drug (e.g., tablet, capsule, syrup).
    - price (float): The price of the drug.

    Returns:
    - JSON object containing the details of the newly added drug.

    Raises:
    - 400 Bad Request: If any required attribute is missing in the request body or if the drug already exists in the database.
    """
    # Check the content type of the request
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Check for required attributes in the request body
    for key in [
        "commercialName",
        "activeIngredient",
        "distributor",
        "dose",
        "form",
        "price",
    ]:
        val = data.get(key, None)
        if not val:
            return jsonify({"error": f"Missing {key}"}), 400

    # Filter out any non-existing attributes for the Drug model
    drug_data = data.copy()
    for key in data:
        if not hasattr(Drug, key):
            drug_data.pop(key)

    # Check if the drug already exists in the database
    drug = database.search(Drug, **drug_data)
    if drug:
        return jsonify({"error": "Drug already exists"}), 400

    # Create a new Drug instance with the provided data
    new_drug = Drug(**drug_data)

    # Return the details of the newly added drug
    return jsonify(database.get_by_id(Drug, str(new_drug.id)).to_dict())


@api.route("/drug/<uuid:drugId>", methods=["PUT"], strict_slashes=False)
@token_required(["pharmacist"])
def update_drug(drugId, current_user):
    """
    Update details of a specific drug identified by drugId.

    Parameters:
    - drugId (UUID): Unique identifier of the drug to update.
    - current_user (User): The user making the request, with token-based authentication (pharmacist role required).

    Request Body Attributes:
    - Any attributes of the Drug model that need to be updated.

    Returns:
    - JSON object containing the updated details of the drug.

    Raises:
    - 400 Bad Request: If any attribute update fails or if the drug with the specified ID is not found.
    """
    # Retrieve the drug from the database based on the provided drugId
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        # Return a 404 Not Found error if the drug is not found in the database
        return jsonify({"error": "Drug not found"}), 404

    # Check the content type of the request
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Update the attributes of the drug with the provided data
    for key, value in data.items():
        if hasattr(drug, key):
            setattr(drug, key, value)
        else:
            # Return a 400 Bad Request error if any attribute update fails
            return jsonify({"error": f"Invalid attribute: {key}"}), 400

    # Save the changes to the database
    drug.save()

    # Return the updated details of the drug
    return jsonify(database.get_by_id(Drug, str(drugId)).to_dict())


@api.route("/drug/<uuid:drugId>", methods=["DELETE"], strict_slashes=False)
@token_required(["pharmacist"])
def delete_drug(drugId, current_user):
    """
    Delete (archive) a drug identified by drugId.

    Parameters:
    - drugId (UUID): Unique identifier of the drug to delete.
    - current_user (User): The user making the request, with token-based authentication (pharmacist role required).

    Returns:
    - Empty JSON response if the deletion is successful.

    Raises:
    - 404 Not Found: If the drug with the specified ID is not found.
    """
    # Retrieve the drug from the database based on the provided drugId
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        # Return a 404 Not Found error if the drug is not found in the database
        return jsonify({"error": "Drug not found"}), 404

    # Archive the drug
    drug.archive()

    # Return an empty JSON response to indicate successful deletion
    return jsonify({})


# Healthcare Worker Endpoints

@api.route("/hcw", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_hcws(current_user):
    """
    Get all healthcare workers.

    This endpoint returns a list of healthcare workers.

    Available for all roles.

    :param current_user: Current authenticated user (obtained from token)
    :return: JSON response with a list of healthcare workers
    """

    # Retrieve all healthcare workers from the database and convert them to dictionaries
    res = []
    for hcw in database.get_all(HCW):
        role = database.get_by_id(User, hcw.userId).role
        if current_user.role == "admin" or role != "admin":
            hcw = hcw.to_dict()
            hcw['role'] = role
            res.append(hcw)

    # Return a JSON response with the list of healthcare workers
    return jsonify(res)


@api.route("/hcw/<uuid:hcwId>", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
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
    """

    # Retrieve the healthcare worker object from the database based on the provided ID
    hcw = database.get_by_id(HCW, str(hcwId))

    # Check if the healthcare worker exists
    if not hcw:
        return jsonify({"error": "Health Care Worker not found!"}), 404

    # Return a JSON response containing the detailed healthcare worker information
    return jsonify(hcw.to_dict())


@api.route("/hcw", methods=["POST"], strict_slashes=False)
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
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Check for required attributes
    for attr in [
        "firstName",
        "lastName",
        "CIN",
        "licence",
        "workAddress",
        "workNumber",
        "role",
        "email",
    ]:
        val = data.get(attr, None)
        if not val:
            return jsonify({"error": f"Missing {attr}"}), 400

    # Check if the provided email already exists in the database
    if database.search(User, email=data["email"]):
        return jsonify({"error": "Email already exists"}), 409

    # Check if the provided licence number already exists in the database
    if database.search(HCW, licence=data["licence"]):
        return jsonify({"error": "Licence number already exists"}), 409

    # Create a new healthcare worker object
    hcw = HCW(
        firstName=data["firstName"],
        lastName=data["lastName"],
        CIN=data["CIN"],
        licence=data["licence"],
        speciality=data.get("speciality"),
        workAddress=data["workAddress"],
        workNumber=data["workNumber"],
        role=data["role"],
        email=data["email"],
    )

    # Save the healthcare worker object to the database
    hcw.save()

    # Return a JSON response with the newly added healthcare worker's information
    return jsonify(hcw.to_dict()), 201


@api.route("/hcw/<uuid:hcwId>", methods=["PUT"], strict_slashes=False)
@token_required([])
def update_hcw(hcwId, current_user):
    """
    Update information for a specific healthcare worker.

    This endpoint allows administrators to update the information of a healthcare worker in the system.
    The request should include the attributes to be updated in JSON format or form data.
    Any provided attributes will overwrite the existing values.

    :param hcwId: The UUID of the healthcare worker to update information for.
    :type hcwId: str
    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response with the updated healthcare worker's information or an error message.
    :rtype: flask.Response
    :raises 400: If any of the required attributes are missing in the request.
    :raises 404: If the specified healthcare worker ID is not found in the database.
    :raises 403: If the user does not have sufficient privileges to access the information.
    :raises 409: If the licence number or email address already exists in the database.
    """

    # Retrieve the healthcare worker object from the database based on the provided ID
    hcw = database.get_by_id(HCW, str(hcwId))

    # Check if the healthcare worker exists
    if not hcw:
        return jsonify({"error": "Health Care Worker not found!"}), 404

    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Update the attributes of the healthcare worker
    for key, value in data.items():
        setattr(hcw, key, value)

    # Save the updated healthcare worker object to the database
    hcw.save()

    # Return a JSON response with the updated healthcare worker's information
    return jsonify(hcw.to_dict())


@api.route("/hcw/<uuid:hcwId>", methods=["DELETE"], strict_slashes=False)
@token_required([])
def delete_hcw(hcwId, current_user):
    """
    Delete (archive) a healthcare worker from the system.

    This endpoint allows administrators to delete (archive) a healthcare worker from the system.
    The healthcare worker with the specified ID will be marked as deleted/archived in the database.

    :param hcwId: The UUID of the healthcare worker to delete.
    :type hcwId: str
    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: An empty JSON response if the deletion is successful.
    :rtype: flask.Response
    :raises 404: If the specified healthcare worker ID is not found in the database.
    """

    # Retrieve the healthcare worker object from the database based on the provided ID
    hcw = database.get_by_id(HCW, str(hcwId))

    # Check if the healthcare worker exists
    if not hcw:
        return jsonify({"error": "Health Care Worker not found!"}), 404

    # Archive the healthcare worker
    hcw.archive()

    # Return an empty JSON response to indicate successful deletion
    return jsonify({})

# Testing Access Endpoints

@api.route("/test/admin", methods=["GET"], strict_slashes=False)
@token_required(["admin"])
def test_admin_access(current_user):
    """
    Test endpoint for admin access.

    This endpoint is restricted to users with the 'admin' role.

    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response confirming admin access.
    :rtype: flask.Response
    """
    return jsonify({"message": "Admin access granted"})


@api.route("/test/doctor", methods=["GET"], strict_slashes=False)
@token_required(["doctor"])
def test_doctor_access(current_user):
    """
    Test endpoint for doctor access.

    This endpoint is restricted to users with the 'doctor' role.

    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response confirming doctor access.
    :rtype: flask.Response
    """
    return jsonify({"message": "Doctor access granted"})


@api.route("/test/nurse", methods=["GET"], strict_slashes=False)
@token_required(["nurse"])
def test_nurse_access(current_user):
    """
    Test endpoint for nurse access.

    This endpoint is restricted to users with the 'nurse' role.

    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response confirming nurse access.
    :rtype: flask.Response
    """
    return jsonify({"message": "Nurse access granted"})


@api.route("/test/pharmacist", methods=["GET"], strict_slashes=False)
@token_required(["pharmacist"])
def test_pharmacist_access(current_user):
    """
    Test endpoint for pharmacist access.

    This endpoint is restricted to users with the 'pharmacist' role.

    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response confirming pharmacist access.
    :rtype: flask.Response
    """
    return jsonify({"message": "Pharmacist access granted"})


@api.route("/test/patient", methods=["GET"], strict_slashes=False)
@token_required(["patient"])
def test_patient_access(current_user):
    """
    Test endpoint for patient access.

    This endpoint is restricted to users with the 'patient' role.

    :param current_user: The current authenticated user object obtained from the token.
    :type current_user: User
    :return: A JSON response confirming patient access.
    :rtype: flask.Response
    """
    return jsonify({"message": "Patient access granted"})
