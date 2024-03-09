from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Prescription(BM, Base):
    __tablename__ = "prescriptions"

    prescribedById = Column(String(40), ForeignKey("hcws.id"))
    prescribedBy = relationship("HCW", foreign_keys=[prescribedById])

    filledById = Column(String(40), ForeignKey("hcws.id"))
    filledBy = relationship("HCW", foreign_keys=[filledById])

    prescribedForId = Column(String(40), ForeignKey("patients.id"))
    prescribedFor = relationship("Patient", back_populates="prescriptions")

    drugs = relationship("DrugPrescribed", uselist=True, back_populates="prescription")

    status = Column(Boolean, default=False)
    notes = Column(String(2048))
