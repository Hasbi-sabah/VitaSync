from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import BM, Base


class TestResult(BM, Base):
    __tablename__ = "testResults"

    tValidatedById = Column(String(40), ForeignKey("hcws.id"))
    tValidatedBy = relationship("HCW", foreign_keys=[tValidatedById])

    bValidatedById = Column(String(40), ForeignKey("hcws.id"))
    btValidatedBy = relationship("HCW", foreign_keys=[bValidatedById])

    prescribedForId = Column(String(40), ForeignKey("patients.id"))
    prescribedFor = relationship("Patient")

    testRequestId = Column(String(40), ForeignKey("testRequests.id"))
    testRequest = relationship("TestRequest", back_populates='results')

    notes = Column(String(2048))