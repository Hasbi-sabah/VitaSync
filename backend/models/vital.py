from sqlalchemy import Column, Double, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Vital(BM, Base):
    """
    Vital model represents the vital signs and health measurements of patients.
    """

    __tablename__ = "vitals"

    # Foreign keys and relationships
    takenById = Column(
        String(40), ForeignKey("hcws.id")
    )  # ID of the HCW who took the vital signs
    takenBy = relationship("HCW")  # Relationship with the HCW model

    takenForId = Column(
        String(40), ForeignKey("patients.id")
    )  # ID of the patient the vitals were taken for
    takenFor = relationship("Patient")  # Relationship with the Patient model

    status = Column(
        Boolean, default=True
    )  # Status indicating normal or abnormal vitals
    temp = Column(Double)  # Temperature measurement
    bp = Column(String(40))  # Blood pressure measurement
    bpm = Column(Integer)  # Beats per minute (heart rate)
    weight = Column(Double)  # Weight measurement
    height = Column(Double)  # Height measurement
    glucose = Column(Double)  # Glucose level measurement
    custom = Column(String(2048))  # Custom additional data for vitals
    notes = Column(String(2048))  # Additional notes related to the vitals
