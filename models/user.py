from sqlalchemy import Column, Integer, String
from models.base import BM, Base
import secrets


class User(BM, Base):
    __tablename__ = "users"

    columns = ['username', 'password', 'role', 'email', 'profileId']
    
    username = Column(String(60))
    password = Column(String(60))
    role = Column(String(20))
    email = Column(String(250))
    profileId = Column(String(40))


    def __init__(self, **kwargs):
        """initializes city of users"""
        if not kwargs.get('username', None):
            email = kwargs.get('email', None)
            if email:
                kwargs['username'] = email.split('@')[0]
        if not kwargs.get('password', None):
            kwargs['password'] = secrets.token_urlsafe(10)
        super().__init__(**kwargs)
