from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class DrugVersion(BM, Base):
    __tablename__ = "drugVersions"

    drugId = Column(String(40), ForeignKey("drugs.id"))
    drug = relationship("Drug", back_populates="versions")

    dose = Column(String(250))
    form = Column(String(250))
    status = Column(Boolean)  # on / off market
