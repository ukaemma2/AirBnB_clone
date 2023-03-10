#!/usr/bin/python3

"""Bsae model that define all common
    attributes/method for other class
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """represents the BaseModel of the HBnB project."""

    def __int__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of attributs.
        """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, time_format)
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
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict['created_at'] = self.updated_at.isoformat()
        rdict['__class__'] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)
