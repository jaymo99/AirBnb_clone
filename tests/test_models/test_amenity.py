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

    def test_amenity_init(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertIsInstance(self.amenity.name, str)
