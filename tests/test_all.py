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

    def TestKwargs(self):
        ''' Test Kwargs'''
        temp_dict = {"updated_at": "2021-11-01T22:14:420127",
                    "created_at": "2021-11-01T22:14:420127",
                    "id": "123abc",
                    "__class__": "BaseModel"}
        mbt = BaseModel(**temp_dict)
        self.assertEqual(mbt.id, "123abc")
        self.assertIsInstance(mbt, BaseModel)
        self.assertIsInstance(mbt.created_at, datetime.datetime)
        self.assertIsInstance(mbt.updated_at, datetime.datetime)
        self.assertIsInstance(mbt.to_dct(), dict)

    def TestStr(self):
        ''' Test Str '''
        tmb = BaseModel()
        self.assertEqual(str(tmb), "[BaseModel] ({}) {}".format
                                    (b.id, b.__dict__))
        
if __name__ == '__main__':
    unittest.main()
