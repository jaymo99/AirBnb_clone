#!/usr/bin/python3
'''File Storage module'''

import json


class FileStorage():
    '''serializes instances to a JSON file and
    deserializes JSON file to instances
    '''
    __file_path = "file.json"
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
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
