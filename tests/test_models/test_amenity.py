#!/usr/bin/python3
""" """
from os import getenv
from models.amenity import Amenity
from tests.test_models.test_base_model import Test_BaseModel


class Test_Amenity(Test_BaseModel):
    """ """
    if getenv("HBNB_TYPE_STORAGE") != "db":
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "Amenity"
            self.value = Amenity

        def test_name2(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.name), str)
