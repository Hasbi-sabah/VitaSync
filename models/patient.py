from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.base import BM, Base
from models.user import User


class Patient(BM, Base):
    __tablename__ = "patients"

    firstName = Column(String(60))
    lastName = Column(String(60))
    CIN = Column(String(20))  # identity card number
    sex = Column(String(20))
    birthDate = Column(String(60))
    phoneNumber = Column(Integer)
    address = Column(String(2048))
    medicalInfo = relationship("MedInfo", uselist=False, back_populates="patient")
    prescriptions = relationship(
        "Prescription", uselist=True, back_populates="prescribedFor"
    )
    vaccines = relationship("Vaccine", uselist=True, back_populates="administeredFor")
    records = relationship("Record", uselist=True, back_populates="patient")
    userId = Column(String(40))


    def __init__(self, **kwargs):
        """initializes city of paitents"""
        userDict = {}
        for key, value in kwargs.items():
            if key in User.columns:
                userDict[key] = value
        super().__init__(**kwargs)
        userDict['profileId'] = self.id
        user = User(**userDict)
        setattr(self, 'userId', user.id)
