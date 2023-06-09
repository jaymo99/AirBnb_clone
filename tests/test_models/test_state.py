import unittest

from models import storage
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = State()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_state_init(self):
        self.assertIsInstance(self.state, State)
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertIsInstance(self.state.name, str)
