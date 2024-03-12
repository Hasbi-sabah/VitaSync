from sqlalchemy import Column, String
from models.base import BM, Base


class HCW(BM, Base):
    __tablename__ = "hcws"

    columns = ['firstName', 'lastName', 'CIN', 'licence', 'role', 'workAddress']
    
    firstName = Column(String(60))
    lastName = Column(String(60))
    CIN = Column(String(20))  # identity card number
    licence = Column(String(20))  # medical licence number
    role = Column(String(20))  # could be doc, nurse, pharmacist
    workAddress = Column(String(2048))
    # TODO: other login columns would be added later
