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

        file_directory = os.path.dirname(cls.json_file)
        cls.new_file = os.path.abspath(
                os.path.join(file_directory, "sample.json"))
        cls.storage._FileStorage__file_path = cls.new_file

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.new_file):
            os.remove(cls.new_file)

    def test_storage_init(self):
        self.assertTrue(self.json_file)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        pass
        amenity = Amenity()
        base_model = BaseModel()
        city = City()
        place = Place()
        review = Review()
        state = State()
        user = User()

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
        with open(self.new_file, "r", encoding='utf-8') as f:
            file_contents = f.read()
        self.assertNotIn(f"User.{user.id}", file_contents)

        self.storage.save()
        with open(self.new_file, "r", encoding='utf-8') as f:
            file_contents = f.read()
        self.assertIn(f"User.{user.id}", file_contents)

    def test_reload(self):
        with open(self.new_file, "w", encoding='utf-8') as f:
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

        self.storage.reload()
        base_model = "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4"
        user = "User.a42ee380-c959-450e-ad29-c840a898cfce"
        self.assertIn(base_model, self.storage.all())
        self.assertIn(user, self.storage.all())
