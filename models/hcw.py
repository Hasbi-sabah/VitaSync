from sqlalchemy import Column, String
from models.base import BM, Base
from models.user import User


class HCW(BM, Base):
    __tablename__ = "hcws"

    columns = ['firstName', 'lastName', 'CIN', 'licence', 'workAddress', 'profileId']
    
    firstName = Column(String(60))
    lastName = Column(String(60))
    CIN = Column(String(20))  # identity card number
    licence = Column(String(20))  # medical licence number
    workAddress = Column(String(2048))
    profileId = Column(String(40))

    def __init__(self, **kwargs):
        """initializes hcw"""
        userDict = {}
        for key, value in kwargs.items():
            if key in User.columns:
                userDict[key] = value
        super().__init__(**kwargs)
        userDict['profileId'] = self.id
        user = User(**userDict)
        setattr(self, 'userId', user.id)
        self.save()
