import os
import textwrap
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.json_file = FileStorage._FileStorage__file_path

    def test_storage_init(self):
        self.assertTrue(self.json_file)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        amenity = Amenity()
        base_model = BaseModel()
        city = City()
        place = Place()
        review = Review()
        state = State()
        user = User()

        self.storage.new(amenity)
        self.storage.new(base_model)
        self.storage.new(city)
        self.storage.new(place)
        self.storage.new(review)
        self.storage.new(state)
        self.storage.new(user)
        self.assertIn(f"Amenity.{amenity.id}", self.storage.all())
        self.assertIn(f"BaseModel.{base_model.id}", self.storage.all())
        self.assertIn(f"City.{city.id}", self.storage.all())
        self.assertIn(f"Place.{place.id}", self.storage.all())
        self.assertIn(f"Review.{review.id}", self.storage.all())
        self.assertIn(f"State.{state.id}", self.storage.all())
        self.assertIn(f"User.{user.id}", self.storage.all())

    def test_save(self):
        self.storage.save()
        user = User()

        self.assertTrue(os.path.exists(self.json_file))
        with open(self.json_file, "r", encoding='utf-8') as f:
            file_contents = f.read()
        self.assertNotIn(f"User.{user.id}", file_contents)

        self.storage.new(user)
        self.storage.save()
        with open(self.json_file, "r", encoding='utf-8') as f:
            file_contents = f.read()
        self.assertIn(f"User.{user.id}", file_contents)

    def test_reload(self):
        storage_2 = FileStorage()
        file_directory = os.path.dirname(self.json_file)
        new_file = os.path.abspath(os.path.join(file_directory, "sample.json"))
        storage_2._FileStorage__file_path = new_file

        with open(new_file, "w", encoding='utf-8') as f:
            sample =\
            '''
            {
                "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {
                    "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4",
                    "updated_at": "2017-09-28T21:11:14.333862",
                    "created_at": "2017-09-28T21:11:14.333852",
                    "__class__": "BaseModel"
                },
                "User.a42ee380-c959-450e-ad29-c840a898cfce": {
                    "id": "a42ee380-c959-450e-ad29-c840a898cfce",
                    "updated_at": "2017-09-28T21:11:15.504296",
                    "created_at": "2017-09-28T21:11:15.504287",
                    "__class__": "User",
                    "first_name": "James",
                    "last_name": "Kariuki"
                }
            }
            '''
            f.write(textwrap.dedent(sample))
        
        storage_2.reload()
        self.assertIn("BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", storage_2.all())
        self.assertIn("User.a42ee380-c959-450e-ad29-c840a898cfce", storage_2.all())
        if os.path.exists(new_file):
            os.remove(new_file)
