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
        all_objs = storage.all()
        obj_key = f"Review.{cls.review.id}"
        if obj_key in all_objs:
            del all_objs[obj_key]

    def test_review_init(self):
        self.assertIsInstance(self.review, Review)
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertIsInstance(self.review.place_id, str)
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertIsInstance(self.review.user_id, str)
        self.assertTrue(hasattr(self.review, "text"))
        self.assertIsInstance(self.review.text, str)
