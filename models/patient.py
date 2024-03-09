from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Patient(BM, Base):
    __tablename__ = "patients"

    firstName = Column(String(60))
    lastName = Column(String(60))
    CIN = Column(String(20))  # identity card number
    sex = Column(String(20))
    birthDate = Column(DateTime)
    phoneNumber = Column(Integer)
    email = Column(String(250))
    address = Column(String(2048))

    medicalInfo = relationship("MedInfo", uselist=False, back_populates="patient")
    prescriptions = relationship(
        "Prescription", uselist=True, back_populates="prescribedFor"
    )
    vaccines = relationship("Vaccine", uselist=True, back_populates="administeredFor")
    records = relationship("Record", uselist=True, back_populates="patient")
    # TODO: other login columns would be added later

    def __init__(self, **kwargs):
        """initializes city"""
        super().__init__(**kwargs)
