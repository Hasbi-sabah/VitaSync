from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.patient import Patient
from models.test import Test
from models.test_request import TestRequest

@api.route('/patient/<uuid:patientId>/test_request', methods=['GET'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient', 'technician'])
def get_all_patient_test_requests(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    if current_user.role == 'patient':
        if current_user.profileId != str(patientId):
            return {
                    "error": "Insufficient privileges!"
                }, 403
    return jsonify([test_request.to_dict() for test_request in database.search(TestRequest, requestedForId=str(patientId))])

@api.route('/patient/<uuid:patientId>/test_request', methods=['POST'], strict_slashes=False)
@token_required(['doctor'])
def add_patient_test_request(patientId, current_user):
    patient = database.get_by_id(Patient, str(patientId))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    testIds = data.get('tests', None)
    if not testIds or type(testIds) is not list:
        return jsonify({"error": "Attribute 'tests' must be a list of test IDs"}), 400
    tests = []
    for testId in testIds:
        test = database.get_by_id(Test, objId=testId)
        tests.append(testId) if test else None
    test_request = TestRequest(notes=data.get('notes', None), tests=tests, requestedForId=patientId, requestedById=current_user.profileId)
    return jsonify(database.get_by_id(TestRequest, str(test_request.id)).to_dict())