import unittest

from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(hasattr(base_model, "id"))
        self.assertIsInstance(base_model.id, str)
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertTrue(hasattr(base_model, "updated_at"))
        self.assertIsInstance(base_model.created_at, datetime)

    def test_str(self):
        pass

# A new BaseModel can be created
# Newly created BaseModel has id, created_at, updated_at
# Test that __str__ prints [<class name>] (<self.id>) <self.__dict__>
# Test that `save(self)` updates the public instance attribute `updated_at` with current datetime
# Test that `to_dict(self` returns a dictionary of all keys and values
#       -> The dates should be in iso format
