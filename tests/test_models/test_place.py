import unittest

from models import storage
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.place = Place()

    @classmethod
    def tearDownClass(cls):
        pass
        all_objs = storage.all()
        obj_key = f"Place.{cls.place.id}"
        if obj_key in all_objs:
            del all_objs[obj_key]

    def test_place_init(self):
        self.assertIsInstance(self.place, Place)
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertIsInstance(self.place.city_id, str)
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertIsInstance(self.place.user_id, str)
        self.assertTrue(hasattr(self.place, "name"))
        self.assertIsInstance(self.place.name, str)
        self.assertTrue(hasattr(self.place, "description"))
        self.assertIsInstance(self.place.description, str)
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertIsInstance(self.place.max_guest, int)
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertIsInstance(self.place.latitude, float)
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertIsInstance(self.place.longitude, float)
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertIsInstance(self.place.amenity_ids, list)
