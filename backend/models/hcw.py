from sqlalchemy import Column, String
from models.base import BM, Base
from models.user import User


class HCW(BM, Base):
    __tablename__ = "hcws"
    
    firstName = Column(String(60))
    lastName = Column(String(60))
    CIN = Column(String(20))  # identity card number
    licence = Column(String(20))  # medical licence number
    speciality = Column(String(150))
    workNumber = Column(String(20))
    workAddress = Column(String(2048))
    userId = Column(String(40))

    def __init__(self, **kwargs):
        """initializes hcw"""
        userDict = {}
        for key, value in kwargs.items():
            if key in User.columns:
                userDict[key] = value
        for key in userDict:
            kwargs.pop(key)
        super().__init__(**kwargs)
        userDict['profileId'] = self.id
        user = User(**userDict)
        setattr(self, 'userId', user.id)
        self.save()