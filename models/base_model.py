#!/usr/bin/python3
"""the base model"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """behold string"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """behold save"""
        self.update_at = datetime.now()

    def to_dict(self):
        """behold the dictionary"""
        bndict = self.__dict__.copy()
        bndict['__class__'] = self.__class__.__name__
        bndict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        bndict['updated_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return bndict
