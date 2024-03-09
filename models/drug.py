from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import BM, Base

class Drug(BM, Base):
    __tablename__ = 'drugs'
    versions = relationship("DrugVersion", uselist=True, back_populates="drug")
    commercialName = Column(String(250))
    activeIngredient = Column(String(250))
    description = Column(String(2048))
    
    def __init__(self, **kwargs):
        """initializes city"""
        super().__init__(**kwargs)