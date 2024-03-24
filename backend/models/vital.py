from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Vital(BM, Base):
    __tablename__ = "vitals"
    
    columns = ['status', 'temp', 'bp', 'bpm', 'weight', 'height', 'glucose', 'notes']

    takenById = Column(String(40), ForeignKey("hcws.id"))
    takenBy = relationship("HCW")

    takenForId = Column(String(40), ForeignKey("patients.id"))
    takenFor = relationship("Patient")

    status = Column(Boolean)  # normal or abnormal
    temp = Column(Integer)
    bp = Column(String(40))
    bpm = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    glucose = Column(Integer)
    notes = Column(String(2048))
