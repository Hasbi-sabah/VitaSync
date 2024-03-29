from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Record(BM, Base):
    """Record model to store medical records."""

    __tablename__ = "records"

    # Foreign key references and relationships
    patientId = Column(
        String(40), ForeignKey("patients.id")
    )  # Patient ID associated with the record
    patient = relationship(
        "Patient", back_populates="records"
    )  # Relationship with Patient model

    vaccineId = Column(
        String(40), ForeignKey("vaccines.id")
    )  # Vaccine ID associated with the record
    vaccine = relationship("Vaccine")  # Relationship with Vaccine model

    vitalsId = Column(
        String(40), ForeignKey("vitals.id")
    )  # Vitals ID associated with the record
    vitals = relationship("Vital")  # Relationship with Vital model

    procedureId = Column(
        String(40), ForeignKey("procedures.id")
    )  # Procedure ID associated with the record
    procedure = relationship("Procedure")  # Relationship with Procedure model

    prescriptionId = Column(
        String(40), ForeignKey("prescriptions.id")
    )  # Prescription ID associated with the record
    prescription = relationship("Prescription")  # Relationship with Prescription model

    assessedById = Column(
        String(40), ForeignKey("hcws.id")
    )  # HCW ID who assessed the record
    assessedBy = relationship("HCW")  # Relationship with HCW model

    diagnosis = Column(String(2048))  # Diagnosis information in the record
    notes = Column(String(2048))  # Additional notes in the record
