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
                    "error": "Missing Authentication Token!"
                }, 401
            try:
                data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
                user_id = data.get('user_id', None)
                if not user_id:
                    raise Exception("Invalid token")
                
                user = db.get_by_id(User, objId=user_id)
                if not user:
                    return {
                        "error": "User not found!"
                    }, 401

                if user.token != token:
                    return {
                        "error": "Wrong token"
                    }, 401
                if user.role not in allowed_roles + ['admin']:
                    return {
                        "error": "Insufficient privileges!"
                    }, 403

                kwargs['current_user'] = user

            except jwt.ExpiredSignatureError:
                return {
                    "error": "Token has expired!"
                }, 401
            except jwt.InvalidTokenError:
                return {
                    "error": "Invalid token!"
                }, 401
            except Exception as e:
                return {
                    "message": "Something went wrong",
                    "error": str(e)
                }, 500

            return f(*args, **kwargs)

        return decorated
    return decorator
