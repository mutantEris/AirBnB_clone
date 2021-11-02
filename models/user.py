#!/usr/bin/python3
'''Module defining class user'''

from models.base_model import BaseModel


class User(BaseModel):
    '''Class user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
