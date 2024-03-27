from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Appointment(BM, Base):
    __tablename__ = "appointments"

    hcwId = Column(String(40), ForeignKey("hcws.id"))
    hcw = relationship("HCW", back_populates="appointments")

    patientId = Column(String(40), ForeignKey("patients.id"))
    patient = relationship("Patient", back_populates="appointments")

    time = Column(Integer)
    notes = Column(String(2048))