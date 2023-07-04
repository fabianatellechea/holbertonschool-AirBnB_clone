#!/usr/bin/python3
"""class that defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime


class BaseModel:
    """class"""

    def __init__(self):
        """ initialization of public instance attributes """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """ updates the attribute updated_at with the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """ returns a dict containing all keys/values of __dict__ """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
