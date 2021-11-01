#!/usr/bin/python3
"""the base model"""


import uuid
from datetime import datetime
import models


class BaseModel():
    """ Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Method Init"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """behold string"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """behold save"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """behold the dictionary"""
        bndict = self.__dict__.copy()
        bndict['__class__'] = self.__class__.__name__
        bndict['created_at'] = self.created_at.isoformat()
        bndict['updated_at'] = self.created_at.isoformat()
        return bndict
