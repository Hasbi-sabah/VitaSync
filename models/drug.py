from sqlalchemy import Column, String, Boolean, Float
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Drug(BM, Base):
    __tablename__ = "drugs"

    columns = ["commercialName", "activeIngredient", "distributor",
               "description", "dose", "form", "status"]

    commercialName = Column(String(250))
    activeIngredient = Column(String(250))
    distributor = Column(String(250))
    dose = Column(String(250))
    form = Column(String(250))
    status = Column(Boolean, default=True)  # on / off market
    price = Column(Float)
    description = Column(String(2048))
