#!/usr/bin/python3
'''Base model'''

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    '''defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if getattr(self, "created_at", None)\
                    and isinstance(self.created_at, str):
                self.created_at = datetime.strptime(self.created_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.utcnow()
            if getattr(self, "updated_at", None)\
                    and isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(self.updated_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance attribute "updated_at"
        with the current datetime
        '''
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of "__dict__"
        '''
        base_dict = dict(self.__dict__)
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
