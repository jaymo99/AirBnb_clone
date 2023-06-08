import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_initialization(self):
        test_amenity = Amenity()
        self.assertIsInstance(test_amenity, Amenity)
