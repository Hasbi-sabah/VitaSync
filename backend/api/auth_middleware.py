from functools import wraps
import jwt
from flask import request, abort, current_app
from models.user import User
from models import database as db


def token_required(allowed_roles=None):
    """
    Decorator function to require a valid authentication token for accessing protected endpoints.

    :param allowed_roles: List of roles allowed to access the endpoint (default is None).
    :return: Decorator function that checks for a valid token and user role.
    """

    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            """
            Inner function that performs the token validation and role check.

            :param args: Arguments passed to the decorated function.
            :param kwargs: Keyword arguments passed to the decorated function.
            :return: Result of the decorated function or an error response.
            """
            # Extract the token from the Authorization header
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]
            if not token:
                # Return error response if token is missing
                return {"error": "Missing Authentication Token!"}, 401

            try:
                # Decode the token using the SECRET_KEY and validate its authenticity
                data = jwt.decode(
                    token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
                )
                user_id = data.get("user_id", None)
                if not user_id:
                    # Raise exception if user_id is missing in token data
                    raise Exception("Invalid token")

                # Fetch the user from the database based on user_id from the token
                user = db.get_by_id(User, objId=user_id)
                if not user:
                    # Return error response if user is not found
                    return {"error": "User not found!"}, 401

                # Validate the token hash against the user's stored hash
                if not user.check_hash(token, 1):
                    # Return error response if token hash doesn't match
                    return {"error": "Wrong token!"}, 401

                # Check if the user's role is allowed to access the endpoint
                if allowed_roles is not None and user.role not in allowed_roles + [
                    "admin"
                ]:
                    # Return error response for insufficient privileges
                    return {"error": "Insufficient privileges!"}, 403

                # Pass the current_user object to the decorated function's keyword arguments
                kwargs["current_user"] = user

            except jwt.ExpiredSignatureError:
                # Return error response for expired token
                return {"error": "Token has expired!"}, 401
            except jwt.InvalidTokenError:
                # Return error response for invalid token
                return {"error": "Invalid token!"}, 401
            except Exception as e:
                # Return error response for other exceptions
                return {"message": "Something went wrong", "error": str(e)}, 500

            # Call the decorated function with updated arguments and return its result
            return f(*args, **kwargs)

        # Return the decorated inner function
        return decorated

    # Return the decorator function
    return decorator
