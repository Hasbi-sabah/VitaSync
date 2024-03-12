from sqlalchemy import Column, String
from models.base import BM, Base


class User(BM, Base):
    __tablename__ = "users"

    username = Column(String(60))
    password = Column(String(60))
    role = Column(String(20)) # 1 for admin, 2 for hcw, 3 for patient
    email = Column(String(250))


    def __init__(self, **kwargs):
        """initializes city of users"""
        super().__init__(**kwargs)
