#!/usr/bin/python3
'''Test All Unittest'''


import unittest
import datetime
import json
from models.base_model.py import Basemodel
import os


class TestBaseModel(unittest.TestCase):
    '''Test for BaseModel'''

    def test_tbm(self):
        ''' Test BaseModel'''
        tbm = BaseModel()
        selfassertIsInstance(tbm.id, str)
        tbm.id = 5
        self.assertIsInstance(tbm, BaseModel)
        self.assertEqual(5, tbm.id)
        self.assertIsInstance(tbm.created_at, datetime.datetime)
        self.assertIsInstance(tbm.updated_at, datetime.datetime)
        self.assertIsInstance(tbm.to_dict(), dict)
