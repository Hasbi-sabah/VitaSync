from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base import BM, Base


class MedInfo(BM, Base):
    """A class representing Medical Information (MedInfo) for patients."""

    __tablename__ = "medInfos"

    # Attributes
    patientId = Column(
        String(40), ForeignKey("patients.id")
    )  # ID of the associated patient
    patient = relationship(
        "Patient", back_populates="medicalInfo"
    )  # Relationship with Patient model

    allergies = Column(String(2048))  # Patient's allergies information
    conditions = Column(String(2048))  # Patient's medical conditions information
    notes = Column(
        String(2048)
    )  # Additional notes related to patient's medical information
