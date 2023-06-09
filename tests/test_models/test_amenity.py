import unittest

from models import storage
from models.amenity import Amenity


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

    def test_initialization(self):
        self.assertIsInstance(self.amenity, Amenity)
