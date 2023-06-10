import unittest

from models import storage
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.city = City()

    @classmethod
    def tearDownClass(cls):
        pass
        all_objs = storage.all()
        obj_key = f"City.{cls.city.id}"
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()

    def test_city_init(self):
        self.assertIsInstance(self.city, City)
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertIsInstance(self.city.state_id, str)
        self.assertTrue(hasattr(self.city, "name"))
        self.assertIsInstance(self.city.name, str)
