#!/usr/bin/python3
""" """
from os import getenv
from models.review import Review
from tests.test_models.test_base_model import Test_BaseModel


class Test_Review(Test_BaseModel):
    """ """
    if getenv("HBNB_TYPE_STORAGE") != "db":
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "Review"
            self.value = Review

        def test_place_id(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.place_id), str)

        def test_user_id(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.user_id), str)

        def test_text(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.text), str)
