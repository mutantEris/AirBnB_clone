#!/usr/bin/python3
'''Test All Unittest'''

import unittest
import datetime
import json
from models.base_model.py import Basemodel

class TestBaseModel(unittest.TestCase):
    '''Test for BaseModel'''

    def test_tbm_exists(self):
    ''' Test to see if tbm was created as an instance'''
        self.tbm = BaseModel()
        self.assertTrue(tbm)

    def test_tbm_equal_BaseModel(self):
    ''' Test to see if tbm is equal to BaseModel'''
        self.assertIsInstance(self.tbm, BaseModel)

    def test_ids(self):
    ''' test ids '''
        self.mbt = BaseModel()
        self.assertNotEqual(self.tbm.id, self.mbt.id)

    def test_created_at(self):
    ''' test created_at '''
        self.assertIsInstance(self.tbm.created_at, datetime.datetime)

    def test_updated_at(self):
    ''' testing updated_at '''
        self.assertIsInstance(self.tbm.updated_at, datetime.datetime)

    def test_str_(self):
    ''' test string '''

    def test_dict(self):
    ''' test dict'''
