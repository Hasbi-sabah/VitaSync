from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import models
from datetime import datetime

Base = declarative_base()


class BM:
    id = Column(String(40), primary_key=True)
    created_at = Column(Integer)
    modified_at = Column(Integer)
    archived = Column(Boolean, default=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in ["__class__", "id", "modified_at", "created_at"]:
                setattr(self, key, value)
        setattr(self, 'created_at', int(datetime.now().timestamp()))
        setattr(self, 'modified_at', int(datetime.now().timestamp()))
        setattr(self, "id", str(uuid4()))
        self.save()

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        setattr(self, 'modified_at', int(datetime.now().timestamp()))
        models.database.new(self)
        models.database.save()

    def delete(self):
        """delete the current instance from the storage"""
        models.database.delete(self)
        
    def archive(self):
        setattr(self, 'archived', True)
        self.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict