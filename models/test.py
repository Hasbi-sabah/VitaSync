from sqlalchemy import Column, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Test(BM, Base):
    __tablename__ = "tests"
    
    columns = ['name', 'type', 'sampleType', 'instructions', 'price', 'description']
    
    name = Column(String(250))
    type = Column(String(50))
    sampleType = Column(String(250))
    instructions = Column(String(250))
    price = Column(Float)
    description = Column(String(2048))