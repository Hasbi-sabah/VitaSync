from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Vaccine(BM, Base):
    """
    Vaccine model represents information about administered vaccines.
    """

    __tablename__ = "vaccines"

    # Foreign keys and relationships
    administeredForId = Column(
        String(40), ForeignKey("patients.id")
    )  # ID of the patient receiving the vaccine
    administeredFor = relationship(
        "Patient", back_populates="vaccines"
    )  # Relationship with the Patient model

    administeredById = Column(
        String(40), ForeignKey("hcws.id")
    )  # ID of the HCW administering the vaccine
    administeredBy = relationship("HCW")  # Relationship with the HCW model

    drugId = Column(
        String(60), ForeignKey("drugs.id")
    )  # ID of the drug used for the vaccine
    drug = relationship("Drug", uselist=True)  # Relationship with the Drug model

    notes = Column(String(2048))  # Additional notes about the vaccine administration
