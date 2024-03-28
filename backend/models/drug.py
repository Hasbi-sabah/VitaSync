from sqlalchemy import Column, String, Boolean, Double
from models.base import BM, Base


class Drug(BM, Base):
    """A class to represent pharmaceutical drugs."""

    __tablename__ = "drugs"

    commercialName = Column(String(250))  # Commercial name of the drug
    activeIngredient = Column(String(250))  # Active ingredient(s) in the drug
    distributor = Column(String(250))  # Name of the distributor or manufacturer
    dose = Column(String(250))  # Dosage information for the drug
    form = Column(String(250))  # Formulation of the drug (e.g., tablet, capsule)
    status = Column(Boolean, default=True)  # Current market status of the drug (on/off)
    price = Column(Double)  # Price of the drug
    description = Column(
        String(2048)
    )  # Description or additional information about the drug
