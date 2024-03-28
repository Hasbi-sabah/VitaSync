from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Procedure(BM, Base):
    """Procedure model to store information about medical procedures."""

    __tablename__ = "procedures"

    # Foreign key references and relationships
    prescribedById = Column(
        String(40), ForeignKey("hcws.id")
    )  # Prescribed by HCW (doctor)
    prescribedBy = relationship(
        "HCW", foreign_keys=[prescribedById]
    )  # Relationship with HCW model

    performedById = Column(
        String(40), ForeignKey("hcws.id")
    )  # Performed by HCW (medical staff)
    performedBy = relationship(
        "HCW", foreign_keys=[performedById]
    )  # Relationship with HCW model

    patientId = Column(
        String(40), ForeignKey("patients.id")
    )  # Patient ID for whom the procedure is performed
    patient = relationship("Patient")  # Relationship with Patient model

    status = Column(
        Boolean, default=False
    )  # Status of the procedure (completed or not)
    name = Column(String(150))  # Name of the procedure
    notes = Column(String(2048))  # Additional notes for the procedure
