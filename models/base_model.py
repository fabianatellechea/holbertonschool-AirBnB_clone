#!/usr/bin/python3
""" """
import uuid
from datetime import datetime


class BaseModel:
    """ """
    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """ """
        self.update_at = datetime.now()
