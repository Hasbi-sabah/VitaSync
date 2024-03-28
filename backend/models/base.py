from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models

# Declare a base class for SQLAlchemy models
Base = declarative_base()


# Define the base model class with common attributes and methods
class BM:
    """Define columns for the base model"""

    id = Column(
        String(40), primary_key=True, index=True
    )  # Unique identifier for each instance
    created_at = Column(Integer)  # Timestamp for creation time
    modified_at = Column(Integer)  # Timestamp for last modification time
    archived = Column(
        Boolean, default=False
    )  # Flag to indicate if the instance is archived

    def __init__(self, **kwargs):
        """Initialize the instance with provided keyword arguments"""
        for key, value in kwargs.items():
            # Set instance attributes from kwargs, excluding certain reserved keys
            if key not in ["__class__", "id", "modified_at", "created_at"]:
                setattr(self, key, value)
        # Set the creation and modification timestamps
        setattr(self, "created_at", int(datetime.now().timestamp()))
        setattr(self, "modified_at", int(datetime.now().timestamp()))
        # Generate a unique ID for the instance
        setattr(self, "id", str(uuid4()))
        self.save()  # Save the instance after initialization

    def save(self):
        """Update the 'modified_at' attribute with the current datetime and save the instance."""
        setattr(self, "modified_at", int(datetime.now().timestamp()))
        models.database.new(self)  # Add the instance to the database session
        models.database.save()  # Save changes to the database

    def delete(self):
        """Delete the current instance from the storage."""
        models.database.delete(self)  # Delete the instance from the database

    def archive(self):
        """Set the 'archived' attribute to True and save the instance."""
        setattr(self, "archived", True)
        self.save()  # Save the instance after archiving

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        from api.base import (
            timestamp_to_str,
        )  # Import a function for timestamp conversion

        new_dict = {}
        for key, value in self.__dict__.items():
            # Check the type of the attribute value and format it accordingly
            if isinstance(value, (int, float, str, bool, list, dict, tuple)):
                if key in ["created_at", "modified_at", "time"]:
                    value = timestamp_to_str(
                        value, "%Y-%m-%d at %I:%M %p"
                    )  # Format timestamp to string
                if key == "birthDate":
                    value = timestamp_to_str(
                        value, "%Y-%m-%d"
                    )  # Format birth date to string
                new_dict[key] = value
        return new_dict  # Return the dictionary representation of the instance
