import unittest

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()

    @classmethod
    def tearDownClass(cls):
        pass
        all_objs = storage.all()
        obj_key = f"Amenity.{cls.amenity.id}"
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()

    def test_amenity_init(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertIsInstance(self.amenity.name, str)
