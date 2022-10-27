#!/usr/bin/python3
"""defines the BaseModel Class"""
import models
from uuid import uuid4


class BaseModel:
    "Represents the basemodel of the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused
            **kwargs (dict): key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = dateime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the print representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}".format(clname, self.id, self.__dict__)
