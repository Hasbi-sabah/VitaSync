from typing import Any
from sqlalchemy import Column, Integer, String
from models.base import BM, Base
import secrets
import bcrypt


class User(BM, Base):
    __tablename__ = "users"

    columns = ['username', 'password', 'role', 'email', 'profileId']
    
    username = Column(String(60))
    password = Column(String(60))
    role = Column(String(20))
    email = Column(String(250))
    profileId = Column(String(40))
    token = Column(String(1024))


    def __init__(self, **kwargs):
        """initializes city of users"""
        if not kwargs.get('username', None):
            email = kwargs.get('email', None)
            if email:
                kwargs['username'] = email.split('@')[0]
        if not kwargs.get('password', None):
            kwargs['password'] = secrets.token_urlsafe(10)
        super().__init__(**kwargs)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'username':
            print('username:', __value)
        if __name == 'password':
            print('password:', __value)
            __value = bcrypt.hashpw(__name.encode('utf-8'), bcrypt.gensalt())
        return super().__setattr__(__name, __value)
    
    def check_hash(self, password):
        return bcrypt.checkpw(self.password.encode('utf-8'), password.encode('utf-8'))
