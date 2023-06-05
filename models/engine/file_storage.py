#!/usr/bin/python3
'''FileStorage module'''

import os
import json


class FileStorage():
    '''serializes instances to a JSON file and
    deserializes JSON file to instances
    '''
    pwd = os.path.dirname(__file__)

    __file_path = os.path.abspath(os.path.join(pwd, "file.json"))
    __objects = {}

    def all(self):
        '''returns a dictionary of all stored objects'''
        return self.__objects

    def new(self, obj):
        '''sets new object in self.__objects'''
        cls_name = obj.__class__.__name__
        new_key = f"{cls_name}.{obj.id}"
        self.__objects[new_key] = obj

    def save(self):
        '''serializes stored objects to a JSON file'''
        with open(self.__file_path, "w", encoding='utf-8') as f:
            new_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(new_dict, f, indent=4)

    def reload(self):
        '''deserializes a JSON file to self.__objects'''
        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                reloaded = json.load(f)
                for key, value in reloaded.items():
                    cls_name = value["__class__"]
                    cls = locals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
