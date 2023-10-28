#!/usr/bin/python3
""" """
import unittest
from os import getenv
from MySQLdb import connect
from subprocess import call
from models.city import City
from tests.test_models.test_base_model import Test_BaseModel


class test_City(Test_BaseModel):
    """ """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        pass

    else:
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "City"
            self.value = City

        def test_state_id(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.state_id), str)

        def test_name(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.name), str)
