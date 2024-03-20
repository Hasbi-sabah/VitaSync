from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database
from models.test import Test


@api.route('/test', methods=['GET'] ,strict_slashes=False)
# @token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_all_tests():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    if data:
        res = [test.to_dict() for test in database.search(Test, **data)]
    else:
        res = [test.to_dict() for test in database.get_all(Test)]
    return jsonify(res)


@api.route('/test_lookup', methods=['POST'] ,strict_slashes=False)
# @token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def test_lookup():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    res = [test.to_dict() for test in database.test_lookup(name=data.get('n', ''))]
    return jsonify(res)


@api.route('/test/<uuid:testId>', methods=['GET'], strict_slashes=False)
# @token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def get_test(testId):
    test = database.get_by_id(Test, str(testId))
    if not test:
        return jsonify({"error": "Test not found"}), 404
    return jsonify(test.to_dict())


@api.route('/test', methods=['POST'], strict_slashes=False)
# @token_required(['pharmacist'])
def add_test():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    test = Test(**data)
    return jsonify(database.get_by_id(Test, str(test.id)).to_dict())


@api.route('/test/<uuid:testId>', methods=['PUT'], strict_slashes=False)
# @token_required(['pharmacist'])
def update_test(testId):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    test = database.get_by_id(Test, str(testId))
    if not test:
        return jsonify({"error": "Test not found"}), 404
    for key, value in data.items():
        if key in Test.columns:
            setattr(test, key, value)
    test.save()
    return jsonify(database.get_by_id(Test, str(testId)).to_dict())


@api.route('/test/<uuid:testId>', methods=['DELETE'], strict_slashes=False)
# @token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def delete_test(testId):
    test = database.get_by_id(Test, str(testId))
    if not test:
        return jsonify({"error": "Test not found"}), 404
    test.archive()
    return jsonify({})