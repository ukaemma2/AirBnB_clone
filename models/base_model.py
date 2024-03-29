#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
            Args:
                *args (any): Unused.
                **kwargs (dict): Key/value pairs of attributes.
        """
        time_fomat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_fomat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        returned_dict = self.__dict__.copy()
        returned_dict["created_at"] = self.created_at.isoformat()
        returned_dict["updated_at"] = self.updated_at.isoformat()
        returned_dict["__class__"] = self.__class__.__name__
        return returned_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
