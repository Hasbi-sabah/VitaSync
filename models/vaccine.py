from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class Vaccine(BM, Base):
    __tablename__ = "vaccines"

    administeredForId = Column(String(40), ForeignKey("patients.id"))
    administeredFor = relationship("Patient", back_populates="vaccines")

    administeredById = Column(String(40), ForeignKey("hcws.id"))
    administeredBy = relationship("HCW")

    drugId = Column(String(60), ForeignKey("drugs.id"))
    drug = relationship("Drug", uselist=False)

    notes = Column(String(2048))
