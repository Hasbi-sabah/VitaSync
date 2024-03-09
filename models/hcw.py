from sqlalchemy import Column, String
from models.base import BM, Base

class HCW(BM, Base):
    __tablename__ = 'hcws'
    firstName = Column(String(60))
    lastName = Column(String(60))
    CIN = Column(String(20)) #identity card number
    licence = Column(String(20)) #medical licence number
    role = Column(String(20)) #could be doc, nurse, pharmacist
    workAddress = Column(String(2048))
    # other login columns would be added later
    
    def __init__(self, **kwargs):
        """initializes city"""
        super().__init__(**kwargs)