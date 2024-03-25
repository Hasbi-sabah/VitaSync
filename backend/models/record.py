from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Record(BM, Base):
    __tablename__ = "records"

    columns = ['diagnosis', 'notes']

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

    diagnosis = Column(String(2048))
    notes = Column(String(2048))