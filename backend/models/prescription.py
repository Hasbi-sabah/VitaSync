from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Prescription(BM, Base):
    """Prescription model to store prescription information."""

    __tablename__ = "prescriptions"

    # Foreign key references and relationships
    prescribedById = Column(
        String(40), ForeignKey("hcws.id")
    )  # Prescribed by HCW (doctor)
    prescribedBy = relationship(
        "HCW", foreign_keys=[prescribedById]
    )  # Relationship with HCW model

    filledById = Column(String(40), ForeignKey("hcws.id"))  # Filled by HCW (pharmacist)
    filledBy = relationship(
        "HCW", foreign_keys=[filledById]
    )  # Relationship with HCW model

    prescribedForId = Column(
        String(40), ForeignKey("patients.id")
    )  # Prescribed for Patient
    prescribedFor = relationship(
        "Patient", back_populates="prescriptions"
    )  # Relationship with Patient model

    drugs = relationship(
        "DrugPrescribed", uselist=True, back_populates="prescription"
    )  # Relationship with DrugPrescribed model

    status = Column(
        Boolean, default=False
    )  # Status of the prescription (filled or not)
    notes = Column(String(2048))  # Additional notes for the prescription
