#!/usr/bin/python3
'''
Module used to store objects into Json file
'''

import models
import json

class FileStorage:
    '''Class FileStorage'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns __objects'''

        return self.__objects

    def new(self, obj):
        '''class new'''

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        '''class save'''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

    def reload(self):
        '''class reload'''
