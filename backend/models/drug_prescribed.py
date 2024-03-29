from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base import BM, Base


class DrugPrescribed(BM, Base):
    """A class to represent prescribed drugs in a prescription."""

    __tablename__ = "drugsPrescribed"

    drugId = Column(String(60), ForeignKey("drugs.id"))
    drug = relationship("Drug", uselist=False)  # Define relationship with Drug class

    prescriptionId = Column(String(40), ForeignKey("prescriptions.id"))
    prescription = relationship(
        "Prescription", back_populates="drugs"
    )  # Define relationship with Prescription class

    instructions = Column(String(2048))  # Instructions for taking the prescribed drug
