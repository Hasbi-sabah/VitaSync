from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BM, Base


# Define the Appointment class inheriting from BaseModel (BM) and Base from SQLAlchemy
class Appointment(BM, Base):
    __tablename__ = "appointments"  # Name of the table in the database

    # Define columns for the Appointment table
    hcwId = Column(
        String(40), ForeignKey("hcws.id")
    )  # Foreign key referencing HCWs table
    hcw = relationship(
        "HCW", back_populates="appointments"
    )  # Relationship with HCW entity

    patientId = Column(
        String(40), ForeignKey("patients.id")
    )  # Foreign key referencing Patients table
    patient = relationship(
        "Patient", back_populates="appointments"
    )  # Relationship with Patient entity

    time = Column(Integer)  # Integer field for storing appointment time (timestamp)
    notes = Column(
        String(2048)
    )  # String field for additional notes related to the appointment
