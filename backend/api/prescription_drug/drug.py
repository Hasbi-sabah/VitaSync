import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.drug import Drug
from models.drug_prescribed import DrugPrescribed


@api.route("/prescription_drug/<uuid:drugId>", methods=["GET"], strict_slashes=False)
@token_required(["doctor", "nurse", "pharmacist", "patient"])
def get_prescription_drug(drugId, current_user):
    """
    Retrieve details of a specific prescription drug.

    Parameters:
        drugId (uuid): The ID of the prescription drug to retrieve.
        current_user: The user making the request with appropriate authorization token.

    Returns:
        A JSON response containing the details of the prescription drug.

    Raises:
        404: If the specified prescription drug ID is not found.
        403: If the user has insufficient privileges to access the prescription drug.
    """
    # Retrieve the prescription drug using the provided drugId
    drug = database.get_by_id(DrugPrescribed, str(drugId))

    # Check if the prescription drug exists
    if not drug:
        # Raise a 404 error if the prescription drug is not found
        return jsonify({"error": "Prescription drug not found"}), 404

    # Check user privileges if role is 'patient'
    if (
        current_user.role == "patient"
        and current_user.profileId != drug.prescription.prescribedForId
    ):
        # Raise a 403 error if the user has insufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    # Return a JSON response containing the details of the prescription drug
    return jsonify(drug.to_dict())


@api.route("/prescription_drug/<uuid:drugId>", methods=["PUT"], strict_slashes=False)
@token_required(["doctor"])
def update_prescription_drug(drugId, current_user):
    """
    Update details of a prescription drug.

    Parameters:
        drugId (uuid): The ID of the prescription drug to update.
        current_user: The user making the request with appropriate authorization token.

    Returns:
        A JSON response containing the updated details of the prescription drug.

    Raises:
        404: If the specified prescription drug ID is not found.
        403: If the user has insufficient privileges to update the prescription drug or the drug is already filled.
        404: If the specified drug ID in the update request is not found.
        400: If there is a duplicate drug in the current prescription after the update.
    """
    # Determine the content type of the request
    content_type = request.headers.get("Content-Type")

    # Extract data based on content type
    if content_type == "application/json":
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # Retrieve the prescription drug using the provided drugId
    drug = database.get_by_id(DrugPrescribed, str(drugId))

    # Check if the prescription drug exists
    if not drug:
        # Raise a 404 error if the prescription drug is not found
        return jsonify({"error": "Prescription drug not found"}), 404

    # Check user privileges for updating the drug
    if current_user.role != "admin":
        # Raise a 403 error if the user has insufficient privileges
        if current_user.profileId != drug.prescription.prescribedById:
            return {"error": "Insufficient privileges!"}, 403

        # Check if the prescription is already filled
        if drug.prescription.status:
            return {"error": "Can't edit a filled prescription!"}, 403

    # Process and update the drug data
    for key, value in data.items():
        # Allow updating 'drugId' and 'instructions' only for admin users or all keys for admin users
        if key in ["drugId", "instructions"] or current_user.role == "admin":
            if key == "drugId":
                # Check if the specified drug ID exists
                if not database.get_by_id(Drug, str(data.get("drugId"))):
                    return jsonify({"error": "Drug not found"}), 404

                # Check for duplicate drugs in the prescription after update
                if database.search(
                    DrugPrescribed, prescriptionId=drug.prescriptionId, drugId=value
                ):
                    return (
                        jsonify({"error": "Duplicate drug in current prescription"}),
                        400,
                    )

            # Set attribute values for the drug
            setattr(drug, key, value)

    # Save the updated drug data
    drug.save()

    # Return a JSON response containing the updated details of the prescription drug
    return jsonify(database.get_by_id(DrugPrescribed, str(drugId)).to_dict())


@api.route("/prescription_drug/<uuid:drugId>", methods=["DELETE"], strict_slashes=False)
@token_required(["doctor"])
def delete_prescription_drug(drugId, current_user):
    """
    Delete a prescription drug.

    Parameters:
        drugId (uuid): The ID of the prescription drug to delete.
        current_user: The user making the request with appropriate authorization token.

    Returns:
        A JSON response indicating a successful deletion.

    Raises:
        404: If the specified prescription drug ID is not found.
        403: If the user has insufficient privileges to delete the prescription drug or if the record is too old to delete.
    """
    # Retrieve the prescription drug using the provided drugId
    drug = database.get_by_id(DrugPrescribed, str(drugId))

    # Check if the prescription drug exists
    if not drug:
        # Raise a 404 error if the prescription drug is not found
        return jsonify({"error": "Prescription drug not found"}), 404

    # Check user privileges for deleting the drug
    if current_user.role != "admin":
        # Raise a 403 error if the user has insufficient privileges
        if current_user.profileId != drug.prescription.prescribedById:
            return {"error": "Insufficient privileges!"}, 403

        # Check if the record is too old to delete
        if drug.created_at + (24 * 3600) < time.time():
            return {"error": "Can't delete records after 24h"}, 403

    # Archive the drug record
    drug.archive()

    # Return a JSON response indicating successful deletion
    return jsonify({})
