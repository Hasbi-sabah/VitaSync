from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.base import BM, Base
from models.user import User


class Patient(BM, Base):
    """Patient model to store patient information."""

    __tablename__ = "patients"

    # Columns for patient information
    firstName = Column(String(60))  # First name of the patient
    lastName = Column(String(60))  # Last name of the patient
    CIN = Column(String(20))  # Identity card number of the patient
    sex = Column(String(20))  # Sex/gender of the patient
    birthDate = Column(Integer)  # Birth date of the patient
    phoneNumber = Column(String(20))  # Phone number of the patient
    address = Column(String(2048))  # Address of the patient
    medicalInfo = relationship(
        "MedInfo", uselist=False, back_populates="patient"
    )  # One-to-one relationship with Medical Information
    prescriptions = relationship(
        "Prescription", uselist=True, back_populates="prescribedFor"
    )  # One-to-many relationship with Prescriptions
    vaccines = relationship(
        "Vaccine", uselist=True, back_populates="administeredFor"
    )  # One-to-many relationship with Vaccines
    records = relationship(
        "Record", uselist=True, back_populates="patient"
    )  # One-to-many relationship with Records
    appointments = relationship(
        "Appointment", uselist=True, back_populates="patient"
    )  # One-to-many relationship with Appointments
    userId = Column(String(40))  # Foreign key reference to the User model

    def __init__(self, **kwargs):
        """
        Initialize a Patient object.

        Parameters:
        - **kwargs: Keyword arguments for patient attributes.
        """
        userDict = {}
        for key, value in kwargs.items():
            # Extract user-related attributes from kwargs
            if key in User.columns:
                userDict[key] = value
        for key in userDict:
            # Remove extracted attributes from kwargs
            kwargs.pop(key)
        # Initialize BM attributes
        super().__init__(**kwargs)
        # Set user-related attributes for User model
        userDict["profileId"] = self.id
        userDict["role"] = "patient"
        user = User(**userDict)
        setattr(self, "userId", user.id)
        self.save()
