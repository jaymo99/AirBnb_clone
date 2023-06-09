import os
import unittest
from datetime import datetime

from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = BaseModel()
        pwd = os.path.dirname(__file__)
        cls.json_file = os.path.join(pwd, "../../models/engine/file.json")
        cls.json_file = os.path.normpath(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        pass
        all_objs = storage.all()
        obj_key = f"BaseModel.{cls.model.id}"
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()

    def test_model_creation(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertIsInstance(self.model.created_at, datetime)

    def test_str(self):
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(expected_str, str(self.model))

    def test_save(self):
        model_key = f"BaseModel.{self.model.id}"
        pre_value = self.model.updated_at
        self.model.save()
        post_value = self.model.updated_at
        self.assertNotEqual(pre_value, post_value)

        with open(self.json_file, "r", encoding='utf-8') as f:
            file_content = f.read()
            self.assertIn(model_key, file_content)

    def test_to_dict(self):
        expected_dict = {
                'id': f"{self.model.id}",
                'created_at': f"{datetime.isoformat(self.model.created_at)}",
                'updated_at': f"{datetime.isoformat(self.model.updated_at)}",
                '__class__': 'BaseModel'
                }
        self.assertEqual(expected_dict, self.model.to_dict())
