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
            for key in kwargs:
                if key in ('create_at', 'updated_at'):
                    kwargs[key] = datetime.strptime(kwargs[keys],
                                                   '%Y-%m-%dT%H:%M:%S.%f')
                if key != ('__class__'):
                    setattr(self, key, kwargs([key])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()

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
        bndict['created_at'] = self.created_at.isoformat()
        bndict['updated_at'] = self.created_at.isoformat()
        return bndict
