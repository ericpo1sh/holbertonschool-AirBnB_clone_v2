#!/usr/bin/python3
""" state tests """
import os
import unittest
import pycodestyle
from models import storage
from models.state import State
from models.base_model import BaseModel, Base


class Test_State(unittest.TestCase):
    """ tests for State subclass of BaseModel """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.state1 = State(name="Texas")
        self.state2 = State(name="New Jersey")
        self.state3 = State(**self.state1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.state1
        del self.state2
        del self.state3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests module docstring """
        self.assertTrue(len(State.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/state.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        """ verifies attributes initialized with correct value & type """
        self.assertEqual(type(self.state1.name), str)
        self.assertEqual(type(self.state2.name), str)
        self.assertEqual(type(self.state3.name), str)
        self.assertEqual(self.state1.name, "Texas")
        self.assertEqual(self.state2.name, "New Jersey")
        self.assertEqual(self.state3.name, "Texas")

    def test_type_subclass(self):
        """ tests correct type/subclass heirarchy """
        self.assertEqual(type(self.state1), State)
        self.assertTrue(isinstance(self.state1, State))
        self.assertTrue(issubclass(self.state1.__class__, BaseModel))
        self.assertTrue(issubclass(self.state1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
