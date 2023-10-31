#!/usr/bin/python3
""" review tests """
import os
import unittest
import pycodestyle
from models import storage
from models.review import Review
from models.base_model import BaseModel, Base


class Test_Review(unittest.TestCase):
    """ tests for Review subclass of BaseModel """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.review1 = Review(
            place_id="thingyUUID4",
            user_id="bigboiUUID4",
            text="review text")
        self.review2 = Review(
            place_id="houseUUID4",
            user_id="homieUUID4",
            text="other text"
        )
        self.review3 = Review(**self.review1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.review1
        del self.review2
        del self.review3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests module docstring """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/review.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        """ verifies attributes initialized with correct value & type """
        self.assertEqual(type(self.review1.place_id), str)
        self.assertEqual(type(self.review1.user_id), str)
        self.assertEqual(type(self.review1.text), str)
        self.assertEqual(type(self.review2.place_id), str)
        self.assertEqual(type(self.review2.user_id), str)
        self.assertEqual(type(self.review2.text), str)
        self.assertEqual(type(self.review3.place_id), str)
        self.assertEqual(type(self.review3.user_id), str)
        self.assertEqual(type(self.review3.text), str)
        self.assertEqual(self.review1.place_id, "thingyUUID4")
        self.assertEqual(self.review1.user_id, "bigboiUUID4")
        self.assertEqual(self.review1.text, "review text")
        self.assertEqual(self.review2.place_id, "houseUUID4")
        self.assertEqual(self.review2.user_id, "homieUUID4")
        self.assertEqual(self.review2.text, "other text")
        self.assertEqual(self.review3.place_id, "thingyUUID4")
        self.assertEqual(self.review3.user_id, "bigboiUUID4")
        self.assertEqual(self.review3.text, "review text")

    def test_type_subclass(self):
        """ tests correct type/subclass heirarchy """
        self.assertEqual(type(self.review1), Review)
        self.assertTrue(isinstance(self.review1, Review))
        self.assertTrue(issubclass(self.review1.__class__, BaseModel))
        self.assertTrue(issubclass(self.review1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
