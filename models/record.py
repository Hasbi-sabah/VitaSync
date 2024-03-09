from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Record(BM, Base):
    __tablename__ = "records"

    patientId = Column(String(40), ForeignKey("patients.id"))
    patient = relationship("Patient", back_populates="records")

    vaccineId = Column(String(40), ForeignKey("vaccines.id"))
    vaccine = relationship("Vaccine")

    vitalsId = Column(String(40), ForeignKey("vitals.id"))
    vitals = relationship("Vital")

    procedureId = Column(String(40), ForeignKey("procedures.id"))
    procedure = relationship("Procedure")

    prescriptionId = Column(String(40), ForeignKey("prescriptions.id"))
    prescription = relationship("Prescription")

    assessedById = Column(String(40), ForeignKey("hcws.id"))
    assessedBy = relationship("HCW")

    status = Column(Boolean, default=False)
    notes = Column(String(2048))
