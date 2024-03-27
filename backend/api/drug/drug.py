from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug


@api.route('/drug', methods=['GET'] ,strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
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
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
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


@api.route('/drug_lookup', methods=['GET'] ,strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
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
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Perform drug lookup based on the provided name (if any)
    res = [drug.to_dict() for drug in database.drug_lookup(name=data.get('name', ''))]

    # Return the list of drugs in JSON format
    return jsonify(res)


@api.route('/drug/<uuid:drugId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
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


@api.route('/drug', methods=['POST'], strict_slashes=False)
@token_required(['pharmacist'])
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
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Check for required attributes in the request body
    for key in ["commercialName", "activeIngredient", "distributor", "dose", "form", "price"]:
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


@api.route('/drug/<uuid:drugId>', methods=['PUT'], strict_slashes=False)
@token_required(['pharmacist'])
def update_drug(drugId, current_user):
    """
    Update details of a specific drug identified by drugId.

    Parameters:
    - drugId (UUID): Unique identifier of the drug to update.
    - current_user (User): The user making the request, with token-based authentication (pharmacist role required).

    Request Body Attributes:
    - Any valid attribute of the Drug model can be updated using this endpoint.

    Returns:
    - JSON object containing the updated details of the drug.

    Raises:
    - 404 Not Found: If the drug with the specified ID is not found.
    - 400 Bad Request: If the request contains invalid attributes or the user lacks permission to update certain attributes.
    """
    # Check the content type of the request
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Retrieve the drug from the database based on the provided drugId
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        # Return a 404 Not Found error if the drug is not found in the database
        return jsonify({"error": "Drug not found"}), 404

    # Update the drug attributes based on the request body data
    for key, value in data.items():
        if hasattr(Drug, key):
            # Check for permission to update certain attributes
            if current_user.role != 'admin' and key in ['modified_at', 'id', 'created_at', 'archived']:
                continue
            # Convert price to float if the attribute is 'price'
            if key == 'price':
                value = float(value)
            setattr(drug, key, value)

    # Save the updated drug to the database
    drug.save()

    # Return the updated details of the drug in JSON format
    return jsonify(database.get_by_id(Drug, str(drugId)).to_dict())


@api.route('/drug/<uuid:drugId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_drug(drugId, current_user):
    """
    Delete a drug identified by drugId.

    Parameters:
    - drugId (UUID): Unique identifier of the drug to delete.
    - current_user (User): The user making the request (authentication not required for this endpoint).

    Returns:
    - JSON object with an empty response.

    Raises:
    - 404 Not Found: If the drug with the specified ID is not found.
    """
    # Retrieve the drug from the database based on the provided drugId
    drug = database.get_by_id(Drug, str(drugId))
    if not drug:
        # Return a 404 Not Found error if the drug is not found in the database
        return jsonify({"error": "Drug not found"}), 404

    # Archive the drug (soft delete) in the database
    drug.archive()

    # Return an empty JSON response to indicate successful deletion
    return jsonify({})
