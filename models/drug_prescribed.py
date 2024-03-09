from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base

class DrugPrescribed(BM, Base):
    __tablename__ = 'drugsPrescribed'
    drugId = Column(String(60), ForeignKey('drugs.id'))
    drug = relationship('Drug', uselist=False)
    drugVersionId = Column(String(60), ForeignKey('drugVersions.id'))
    drugVersion = relationship('DrugVersion', uselist=False)
    instructions = Column(String(2048))