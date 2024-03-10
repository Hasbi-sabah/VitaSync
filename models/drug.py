from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Drug(BM, Base):
    __tablename__ = "drugs"

    commercialName = Column(String(250))
    activeIngredient = Column(String(250))
    dose = Column(String(250))
    form = Column(String(250))
    status = Column(Boolean)  # on / off market
    description = Column(String(2048))
