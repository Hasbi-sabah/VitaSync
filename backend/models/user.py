from typing import Any
from sqlalchemy import Column, Integer, String
from models.base import BM, Base
import secrets
import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import current_app


class User(BM, Base):
    """
    User model represents user information and authentication methods.
    """

    __tablename__ = "users"

    # List of columns for serialization
    columns = ["username", "password", "role", "email", "profileId"]

    # User attributes
    username = Column(String(60))  # User's username
    password = Column(String(60))  # Hashed password using bcrypt
    role = Column(String(20))  # User's role (e.g., doctor, nurse, patient)
    email = Column(String(250))  # User's email
    profileId = Column(String(40))  # Profile ID associated with the user
    token = Column(String(500))  # JWT token for authentication

    def __init__(self, **kwargs):
        """
        Initialize User object.

        Args:
        - kwargs: keyword arguments to set user attributes
        """
        super().__init__(**kwargs)
        print("Username: ", self.username)
        print("Password: ", self.password)

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Override setattr method to hash password and token.

        Args:
        - __name: attribute name
        - __value: attribute value
        """
        print(__value)
        if __name == "password" or __name == "token":
            print("password: ", __value)
            __value = bcrypt.hashpw(__value.encode("utf-8"), bcrypt.gensalt())
        return super().__setattr__(__name, __value)

    def check_hash(self, unhashed, flag=0):
        """
        Check if the provided unhashed password/token matches the stored hash.

        Args:
        - unhashed: unhashed password or token
        - flag: flag to indicate whether to check token or password
        Returns:
        - bool: True if match, False otherwise
        """
        hashed = self.token if flag else self.password
        return bcrypt.checkpw(unhashed.encode("utf-8"), hashed.encode("utf-8"))

    def create_jwt(self):
        """
        Create and return a JWT token for user authentication.

        Returns:
        - str: JWT token
        """
        now = datetime.now()
        exp = now + timedelta(hours=24)
        payload = {
            "user_id": self.id,
            "iat": int(now.timestamp()),
            "exp": int(exp.timestamp()),
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
        setattr(self, "token", token)
        self.save()
        return token
