from sqlalchemy import Column, Double, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Vital(BM, Base):
    __tablename__ = "vitals"
    
    columns = ['status', 'temp', 'bp', 'bpm', 'weight', 'height', 'glucose', 'notes']

    takenById = Column(String(40), ForeignKey("hcws.id"))
    takenBy = relationship("HCW")

    takenForId = Column(String(40), ForeignKey("patients.id"))
    takenFor = relationship("Patient")

    status = Column(Boolean, default=True)  # normal or abnormal
    temp = Column(Double)
    bp = Column(String(40))
    bpm = Column(Integer)
    weight = Column(Double)
    height = Column(Double)
    glucose = Column(Double)
    custom = Column(String(2048))
    notes = Column(String(2048))
