import unittest

from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        pass
        all_objs = storage.all()
        obj_key = f"User.{cls.user.id}"
        if obj_key in all_objs:
            del all_objs[obj_key]

    def test_user_init(self):
        email_regex = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertIsInstance(self.user.email, str)
        if self.user.email:
            self.assertRegex(self.user.email, email_regex)
        self.assertTrue(hasattr(self.user, "password"))
        self.assertIsInstance(self.user.password, str)
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertIsInstance(self.user.first_name, str)
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertIsInstance(self.user.last_name, str)
