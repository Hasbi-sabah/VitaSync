from functools import wraps
import jwt
from flask import request, abort, current_app
from models.user import User
from models import database as db


def token_required(allowed_roles=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]
            if not token:
                return {
                    "message": "Authentication Token is missing!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            try:
                data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
                user_id = data.get('user_id')
                if not user_id:
                    raise Exception("Invalid token")
                
                user = db.get_by_id(User, objId=user_id)
                if not user:
                    return {
                        "message": "User not found!",
                        "data": None,
                        "error": "Unauthorized"
                    }, 401

                if allowed_roles and user.role not in allowed_roles:
                    return {
                        "message": "Insufficient privileges!",
                        "data": None,
                        "error": "Unauthorized"
                    }, 403

                kwargs['current_user'] = user

            except jwt.ExpiredSignatureError:
                return {
                    "message": "Token has expired!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            except jwt.InvalidTokenError:
                return {
                    "message": "Invalid token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            except Exception as e:
                return {
                    "message": "Something went wrong",
                    "data": None,
                    "error": str(e)
                }, 500

            return f(*args, **kwargs)

        return decorated
    return decorator
