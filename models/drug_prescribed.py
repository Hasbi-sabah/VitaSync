from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class DrugPrescribed(BM, Base):
    __tablename__ = "drugsPrescribed"

    columns = ['drugId', 'instructions']

    drugId = Column(String(60), ForeignKey("drugs.id"))
    drug = relationship("Drug", uselist=False)

    prescriptionId = Column(String(40), ForeignKey("prescriptions.id"))
    prescription = relationship("Prescription", back_populates="drugs")

    instructions = Column(String(2048))
