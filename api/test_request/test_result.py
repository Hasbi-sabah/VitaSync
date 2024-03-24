from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.test_request import TestRequest
from models.test_result import TestResult

@api.route('/test_request/<uuid:testRequestId>/result', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_test_request_results(testRequestId, current_user):
    test_request = database.get_by_id(TestRequest, str(testRequestId))
    if not test_request:
        return jsonify({"error": "Test Request not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != test_request.requestedForId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([result.to_dict() for result in test_request.results])

@api.route('/test_request/<uuid:testRequestId>/result', methods=['POST'], strict_slashes=False)
@token_required(['doctor'])
def add_test_request_result(testRequestId, current_user):
    test_request = database.get_by_id(TestRequest, str(testRequestId))
    if not test_request:
        return jsonify({"error": "Test Request not found"}), 404
    content_type = request.headers.get('Content-Type')
    data = request.get_json() if content_type == 'application/json' else request.form.to_dict()
    result = TestResult(**data, testRequestId=testRequestId)
    return jsonify(database.get_by_id(TestResult, str(result.id)).to_dict())
