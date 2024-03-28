from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import BM, Base
from models.user import User


class HCW(BM, Base):
    """A class representing Healthcare Workers (HCWs)."""

    __tablename__ = "hcws"

    # HCW attributes
    firstName = Column(String(60))  # First name of the HCW
    lastName = Column(String(60))  # Last name of the HCW
    CIN = Column(String(20))  # Identity card number of the HCW
    licence = Column(String(20))  # Medical licence number of the HCW
    speciality = Column(String(150))  # Speciality or area of expertise of the HCW
    workNumber = Column(String(20))  # Work contact number of the HCW
    workAddress = Column(String(2048))  # Work address of the HCW

    # Relationships
    appointments = relationship("Appointment", uselist=True, back_populates="hcw")
    userId = Column(String(40))  # ID of the associated user

    def __init__(self, **kwargs):
        """Initialize a new HCW object."""
        userDict = {}
        # Extract user-related data from kwargs
        for key, value in kwargs.items():
            if key in User.columns:
                userDict[key] = value
        # Remove user-related data from kwargs
        for key in userDict:
            kwargs.pop(key)
        # Call the parent class constructor
        super().__init__(**kwargs)
        # Create a new User instance associated with this HCW
        userDict["profileId"] = self.id
        user = User(**userDict)
        setattr(self, "userId", user.id)  # Set the userId attribute
        self.save()  # Save the HCW instance to the database
