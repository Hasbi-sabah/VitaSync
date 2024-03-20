from sqlalchemy import JSON, Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class TestRequest(BM, Base):
    __tablename__ = "testRequests"

    requestedById = Column(String(40), ForeignKey("hcws.id"))
    requestedBy = relationship("HCW")

    requestedForId = Column(String(40), ForeignKey("patients.id"))
    requestedFor = relationship("Patient")

    tests = relationship("Test", uselist=True)

    results = relationship("TestResult", uselist=True, back_populates='testRequest')

    notes = Column(String(2048))