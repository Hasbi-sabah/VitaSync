from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.test import Test
from models.test_request import TestRequest


@api.route('/test_request/<uuid:test_requestId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_test_request(testRequestId, current_user):
    test_request = database.get_by_id(TestRequest, str(testRequestId))
    if not test_request:
        return jsonify({"error": "Test Request not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != test_request.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(test_request.to_dict())

@api.route('/test_request/<uuid:testRequestId>', methods=['PUT'], strict_slashes=False)
@token_required(['doctor'])
def update_testRequest(testRequestId, current_user):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    test_request = database.get_by_id(TestRequest, str(testRequestId))
    if not test_request:
        return jsonify({"error": "Test Request not found"}), 404
    if current_user.role != 'admin':
        if current_user.profileId != test_request.requestedById:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    if data.get('notes', None):
        setattr(test_request, 'notes', data.get('notes'))
    testIds = data.get('tests', None)
    if testIds:
        tests = []
        for testId in testIds:
            test = database.get_by_id(Test, objId=testId)
            tests.append(testId) if test else None
        setattr(test_request, 'tests', tests)
    test_request.save()
    return jsonify(database.get_by_id(TestRequest, str(testRequestId)).to_dict())

@api.route('/test_request/<uuid:testRequestId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_testRequest(testRequestId, current_user):
    test_request = database.get_by_id(TestRequest, str(testRequestId))
    if not test_request:
        return jsonify({"error": "Test Request not found"}), 404
    test_request.archive()
    return jsonify({})