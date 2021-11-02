#!/usr/bin/python3
'''Module defining class Review'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Class Review '''
    place_id = ""
    user_id = ""
    text = ""
