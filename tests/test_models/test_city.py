#!/usr/bin/python3
""" city tests """
import os
import unittest
import pycodestyle
from models import storage
from models.city import City


class Test_City(unittest.TestCase):
    """ tests for City subclass of BaseModel """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.city1 = City(name="Philly", state_id="testUUID4")
        self.city2 = City(name="Tulsa", state_id="whatUUID4")
        self.city3 = City(**self.city1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.city1
        del self.city2
        del self.city3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests module docstring """
        self.assertTrue(len(City.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/city.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        """ verifies attributes initialized with correct value & type """
        self.assertEqual(type(self.city1.state_id), str)
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city2.state_id), str)
        self.assertEqual(type(self.city2.name), str)
        self.assertEqual(type(self.city3.state_id), str)
        self.assertEqual(type(self.city3.name), str)
        self.assertEqual(self.city1.state_id, "testUUID4")
        self.assertEqual(self.city1.name, "Philly")
        self.assertEqual(self.city2.state_id, "whatUUID4")
        self.assertEqual(self.city2.name, "Tulsa")
        self.assertEqual(self.city3.state_id, "testUUID4")
        self.assertEqual(self.city3.name, "Philly")


if __name__ == "__main__":
    unittest.main()
