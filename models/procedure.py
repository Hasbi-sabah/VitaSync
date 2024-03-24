from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Procedure(BM, Base):
    __tablename__ = "procedures"

    columns = ['notes']

    prescribedById = Column(String(40), ForeignKey("hcws.id"))
    prescribedBy = relationship("HCW", foreign_keys=[prescribedById])

    performedById = Column(String(40), ForeignKey("hcws.id"))
    performedBy = relationship("HCW", foreign_keys=[performedById])

    patientId = Column(String(40), ForeignKey("patients.id"))
    patient = relationship("Patient")

    status = Column(Boolean, default=False)
    notes = Column(String(2048))
