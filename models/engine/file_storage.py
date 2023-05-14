#!/usr/bin/python3
'''File Storage module'''

import os
import json
from models.base_model import BaseModel


class FileStorage():
    '''serializes instances to a JSON file and
    deserializes JSON file to instances
    '''
    pwd = os.path.dirname(__file__)
    __file_path = os.path.abspath(os.path.join(pwd, '..', '..', 'file.json'))
    __objects = {}

    def all(self):
        '''returns a dictionary containing all objects
        '''
        return self.__objects

    def new(self, obj):
        '''sets/adds an object to a dictionary
        '''
        obj_classname = str(obj.__class__.__name__)
        obj_id = getattr(obj, "id", None)

        if obj_id:
            new_key = obj_classname + '.' + obj_id
            self.__objects[new_key] = obj

    def save(self):
        '''serializes all objects to the JSON file in __file_path
        '''
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        '''deserializes the JSON file in __file_path to __objects
        '''
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                reloaded_objs = json.load(f)
                for key, value in reloaded_objs.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
