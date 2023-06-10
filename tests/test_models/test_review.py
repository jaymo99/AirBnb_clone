import unittest

from models import storage
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = Review()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_review_init(self):
        self.assertIsInstance(self.review, Review)
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertIsInstance(self.review.place_id, str)
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertIsInstance(self.review.user_id, str)
        self.assertTrue(hasattr(self.review, "text"))
        self.assertIsInstance(self.review.text, str)
