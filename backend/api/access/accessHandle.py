from flask import jsonify, request
from api import api
from api.auth_middleware import token_required
from models import database

@api.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Authenticates a user based on provided credentials (username and password).

    This function checks the content type of the request and parses the data accordingly.
    If the content type is JSON, it expects JSON data containing the username and password.
    If the content type is not JSON, it expects form data containing the username and password.

    Parameters:
    - None (Uses data from the request headers and body)

    Returns:
    - JSON object containing authentication token, user role, and user ID if authentication is successful.

    Raises:
    - 400 Bad Request: If the username or password is missing in the request data.
    - 404 Not Found: If the user with the provided username is not found in the database.
    - 401 Unauthorized: If the provided password does not match the user's hashed password.
    """
    # Check the content type of the request to determine how to parse the data
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        # Parse JSON data if content type is JSON
        data = request.get_json()
    else:
        # Parse form data if content type is not JSON
        data = request.form.to_dict()

    # Extract username and password from the data
    username = data.get('username', None)
    if not username:
        # Return error response if username is missing
        return jsonify({"error": "Invalid Credentials"}), 400

    password = data.get('password', None)
    if not password:
        # Return error response if password is missing
        return jsonify({"error": "Invalid Credentials"}), 400

    # Fetch user from the database based on the provided username
    user = database.get_by_username(username=username)
    if not user:
        # Return error response if user is not found
        return jsonify({"error": "User not found"}), 404

    # Check if the provided password matches the user's hashed password
    if not user.check_hash(password):
        # Return error response if password is incorrect
        return jsonify({"error": "Wrong password"}), 401

    # Generate a JWT token for the authenticated user
    token = user.create_jwt()

    # Return the JWT token, user role and Id in a JSON response
    return jsonify({'token': token, 'role': user.role, 'id': user.profileId})

@api.route('/logout', methods=['POST'], strict_slashes=False)
@token_required(['doctor', 'nurse', 'pharmacist', 'patient'])
def logout(current_user):
    """
    Endpoint for user logout.

    This endpoint allows authenticated users to log out by invalidating their JWT token.
    After logout, the token is set to None and the user's data is saved.

    :param current_user: Current authenticated user (obtained from token).
    :return: Empty JSON response indicating successful logout.
    """
    # Set the token attribute of the current user to None
    setattr(current_user, 'token', None)

    # Save the updated user data to the database
    current_user.save()

    # Return an empty JSON response to indicate successful logout
    return jsonify({})
