from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.prescription import Prescription
from models.drug_prescribed import DrugPrescribed


@api.route(
    "/prescription/<uuid:prescriptionId>/drug", methods=["GET"], strict_slashes=False
)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_prescription_drugs(prescriptionId, current_user):
    """
    Get all drugs prescribed in a specific prescription.

    Parameters:
        prescriptionId (uuid): The ID of the prescription for which drugs are to be retrieved.
        current_user: The user making the request with appropriate authorization token.

    Returns:
        A JSON response containing a list of all drugs in the prescription.

    Raises:
        404: If the specified prescription ID is not found.
        403: If the user does not have sufficient privileges to access the prescription.
    """
    # Retrieve the prescription using the provided prescriptionId
    prescription = database.get_by_id(Prescription, str(prescriptionId))

    # Check if the prescription exists
    if not prescription:
        # Raise a 404 error if the prescription is not found
        return jsonify({"error": "Prescription not found"}), 404

    # Check user role and profile ID for authorization
    if (
        current_user.role == "prescription"
        and current_user.profileId != prescription.prescribedForId
    ):
        # Raise a 403 error if the user doesn't have sufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    # Return a JSON response containing a list of drugs in the prescription
    return jsonify([drug.to_dict() for drug in prescription.drugs if not drug.archived])

@api.route(
    "/prescription/<uuid:prescriptionId>/drug_extended", methods=["GET"], strict_slashes=False
)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_all_prescription_drugs_extended(prescriptionId, current_user):
    """
    Get all drugs prescribed in a specific prescription.

    Parameters:
        prescriptionId (uuid): The ID of the prescription for which drugs are to be retrieved.
        current_user: The user making the request with appropriate authorization token.

    Returns:
        A JSON response containing a list of all drugs in the prescription.

    Raises:
        404: If the specified prescription ID is not found.
        403: If the user does not have sufficient privileges to access the prescription.
    """
    # Retrieve the prescription using the provided prescriptionId
    prescription = database.get_by_id(Prescription, str(prescriptionId))

    # Check if the prescription exists
    if not prescription:
        # Raise a 404 error if the prescription is not found
        return jsonify({"error": "Prescription not found"}), 404

    # Check user role and profile ID for authorization
    if (
        current_user.role == "prescription"
        and current_user.profileId != prescription.prescribedForId
    ):
        # Raise a 403 error if the user doesn't have sufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    res = []
    for drug in prescription.drugs:
        if not drug.archived:
            drugDict = drug.to_dict()
            for key in ['commercialName', 'dose', 'form', 'activeIngredient', 'price']:
                drugDict[key] = getattr(drug.drug, key)
            res.append(drugDict)
    print(res)
    # Return a JSON response containing a list of drugs in the prescription
    return jsonify(res)

@api.route(
    "/prescription/<uuid:prescriptionId>/drug", methods=["POST"], strict_slashes=False
)
@token_required(["doctor"])
def add_prescription_drug(prescriptionId, current_user):
    """
    Add a drug to a specific prescription.

    Parameters:
        prescriptionId (uuid): The ID of the prescription to which the drug will be added.
        current_user: The user making the request with appropriate authorization token.

    Returns:
        A JSON response containing the details of the added drug.

    Raises:
        404: If the specified prescription ID is not found.
        400: If required parameters are missing or if there's a duplicate drug in the prescription.
        404: If the specified drug ID is not found.
    """
    # Retrieve the prescription using the provided prescriptionId
    prescription = database.get_by_id(Prescription, str(prescriptionId))

    # Check if the prescription exists
    if not prescription:
        # Raise a 404 error if the prescription is not found
        return jsonify({"error": "Prescription not found"}), 404

    # Get the content type of the request
    content_type = request.headers.get("Content-Type")

    # Extract data based on the content type (JSON or form data)
    data = (
        request.get_json()
        if content_type == "application/json"
        else request.form.to_dict()
    )

    # Validate and extract required data for the new drug
    new_data = {}
    for attr in ["drugId", "instructions"]:
        if not data.get(attr, None):
            # Raise a 400 error if required data is missing
            return jsonify({"error": f"Missing {attr}"}), 400
        new_data[attr] = data.get(attr, None)

    # Retrieve the drug using the provided drugId
    drug = database.get_by_id(Drug, str(data.get("drugId")))

    # Check if the drug exists
    if not drug:
        # Raise a 404 error if the drug is not found
        return jsonify({"error": "Drug not found"}), 404

    # Check for duplicate drugs in the prescription
    if database.search(
        DrugPrescribed, prescriptionId=str(prescriptionId), drugId=drug.id
    ):
        # Raise a 400 error if a duplicate drug is found in the prescription
        return jsonify({"error": "Duplicate drug in current prescription"}), 400

    # Create a new DrugPrescribed instance and add it to the prescription
    drug_prescribed = DrugPrescribed(**new_data, prescriptionId=str(prescriptionId))

    # Return a JSON response containing the details of the added drug
    return jsonify(
        database.get_by_id(DrugPrescribed, str(drug_prescribed.id)).to_dict()
    )
