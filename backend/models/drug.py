from sqlalchemy import Column, Double, String, Boolean, Float
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Drug(BM, Base):
    __tablename__ = "drugs"

    commercialName = Column(String(250))
    activeIngredient = Column(String(250))
    distributor = Column(String(250))
    dose = Column(String(250))
    form = Column(String(250))
    status = Column(Boolean, default=True)  # on / off market
    price = Column(Double)
    description = Column(String(2048))
