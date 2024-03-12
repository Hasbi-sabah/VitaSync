from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BM:
    id = Column(String(40), primary_key=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in ["__class__", "id"]:
                setattr(self, key, value)
        setattr(self, "id", str(uuid4()))
        self.save()

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        models.database.new(self)
        models.database.save()

    def delete(self):
        """delete the current instance from the storage"""
        models.database.delete(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict