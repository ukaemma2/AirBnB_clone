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
                    self.__dict__[key] = v
        else:
            models.storage.new(self)
