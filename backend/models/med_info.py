from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class MedInfo(BM, Base):
    __tablename__ = "medInfos"

    patientId = Column(String(40), ForeignKey("patients.id"))
    patient = relationship("Patient", back_populates="medicalInfo")

    allergies = Column(String(2048))
    consitions = Column(String(2048))
    notes = Column(String(2048))
