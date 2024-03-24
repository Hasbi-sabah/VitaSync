from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.test import Test
from models.test_result import TestResult


@api.route('/test_result/<uuid:testResultId>', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_test_result(testResultId, current_user):
    test_result = database.get_by_id(TestResult, str(testResultId))
    if not test_result:
        return jsonify({"error": "Test Result not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != test_result.patient.userId:
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify(test_result.to_dict())

# @api.route('/test_result/<uuid:testResultId>', methods=['PUT'], strict_slashes=False)
# @token_required(['doctor'])
# def update_testRequest(testResultId, current_user):
#     file = request.files['file']
#     file.save('/results/' + '')
#     content_type = request.headers.get('Content-Type')
#     if content_type == 'application/json':
#         data = request.get_json()
#     else:
#         data = request.form.to_dict()
#     test_result = database.get_by_id(TestResult, str(testResultId))
#     if not test_result:
#         return jsonify({"error": "Test Result not found"}), 404
#     if current_user.role != 'admin':
#         if current_user.profileId != test_result.requestedById:
#             return {
#                     "error": "Insufficient privileges!"
#                 }, 403
#     if data.get('notes', None):
#         setattr(test_result, 'notes', data.get('notes'))
#     testIds = data.get('tests', None)
#     if testIds:
#         tests = []
#         for testId in testIds:
#             test = database.get_by_id(Test, objId=testId)
#             tests.append(testId) if test else None
#         setattr(test_result, 'tests', tests)
#     test_result.save()
#     return jsonify(database.get_by_id(TestResult, str(testResultId)).to_dict())

@api.route('/test_result/<uuid:testResultId>', methods=['DELETE'], strict_slashes=False)
@token_required([])
def delete_testRequest(testResultId, current_user):
    test_result = database.get_by_id(TestResult, str(testResultId))
    if not test_result:
        return jsonify({"error": "Test Result not found"}), 404
    test_result.archive()
    return jsonify({})