import time
from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.procedure import Procedure


@api.route('/procedure/<uuid:procedureId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_procedure(procedureId, current_user):
    """
    Retrieves details of a specific procedure.

    Parameters:
    - procedureId (uuid): The unique identifier of the procedure to retrieve.
    - current_user: The authenticated user making the request.

    Returns:
    - JSON response containing the details of the requested procedure.

    Raises:
    - 404: If the procedure with the given procedureId is not found in the database.
    - 403: If the current user does not have sufficient privileges to access the procedure.
    """
    # Retrieve the procedure from the database using the provided procedureId
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        # Return an error response if the procedure is not found
        return jsonify({"error": "Procedure not found"}), 404

    # Check if the current user has sufficient privileges to access the procedure
    if current_user.role == 'patient' and current_user.profileId != procedure.patientId:
        # Return an error response for insufficient privileges
        return {"error": "Insufficient privileges!"}, 403

    # Return JSON response with the details of the requested procedure
    return jsonify(procedure.to_dict())

@api.route('/procedure/<uuid:procedureId>/perform', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse'])
def procedure_perform(procedureId, current_user):
    """
    Marks a procedure as performed.

    Parameters:
    - procedureId (uuid): The unique identifier of the procedure to mark as performed.
    - current_user: The authenticated user performing the procedure.

    Returns:
    - JSON response containing the details of the updated procedure after marking it as performed.

    Raises:
    - 404: If the procedure with the given procedureId is not found in the database.
    - 409: If the procedure is already marked as performed.
    """
    # Retrieve the procedure from the database using the provided procedureId
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        # Return an error response if the procedure is not found
        return jsonify({"error": "Procedure not found"}), 404

    # Check if the procedure is already marked as performed
    if procedure.status:
        # Return an error response if the procedure is already performed
        return jsonify({"error": "Procedure already performed"}), 409

    # Update the procedure status to performed and set the performedById attribute
    setattr(procedure, 'status', True)
    setattr(procedure, 'performedById', current_user.profileId)
    procedure.save()

    # Return JSON response with the details of the updated procedure
    return jsonify(database.get_by_id(Procedure, str(procedure.id)).to_dict())

@api.route('/procedure/<uuid:procedureId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_procedure(procedureId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        return jsonify({"error": "Procedure not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != procedure.prescribedById:
            return {"error": "Insufficient privileges!"}, 403
        if procedure.created_at + (24 * 3600) < time.time():
            return {"error": "Can't edit records after 24h"}, 403
    for key, value in data.items():
        if current_user.role != 'admin' and key in ['id', 'created_at', 'modified_at', 'archived', 'prescribedById', 'performedById', 'patientId']:
            continue
        if hasattr(procedure, key):
            setattr(procedure, key, value)
    procedure.save()
    return jsonify(database.get_by_id(Procedure, str(procedureId)).to_dict())

@api.route('/procedure/<uuid:procedureId>', methods=['DELETE'], strict_slashes=False)
@token_required(['doctor'])
def delete_procedure(procedureId, current_user):
    """
    Deletes a procedure.

    Parameters:
    - procedureId (uuid): The unique identifier of the procedure to delete.
    - current_user: The authenticated user attempting to delete the procedure.

    Returns:
    - JSON response indicating the successful deletion of the procedure.

    Raises:
    - 404: If the procedure with the given procedureId is not found in the database.
    - 403: If the user does not have sufficient privileges to delete the procedure or if deletion is not allowed after 24 hours.
    """
    # Retrieve the procedure from the database using the provided procedureId
    procedure = database.get_by_id(Procedure, str(procedureId))
    if not procedure:
        # Return an error response if the procedure is not found
        return jsonify({"error": "Procedure not found"}), 404

    # Check if the user has sufficient privileges to delete the procedure
    if current_user.role != 'admin':
        if current_user.profileId != procedure.prescribedById:
            # Return an error response if the user does not have permission to delete the procedure
            return {"error": "Insufficient privileges!"}, 403
        if procedure.created_at + (24 * 3600) < time.time():
            # Return an error response if deletion is not allowed after 24 hours
            return {"error": "Can't delete records after 24h"}, 403

    # Archive the procedure to mark it as deleted
    procedure.archive()

    # Return an empty JSON response indicating successful deletion
    return jsonify({})