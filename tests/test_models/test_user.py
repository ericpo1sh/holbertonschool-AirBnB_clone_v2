#!/usr/bin/python3
""" """
import os
import unittest
import pycodestyle
from models import storage
from models.user import User


class Test_User(unittest.TestCase):
    """ """
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @classmethod
        def setUp(self):
            """ preparation method to be performed before each test """
            self.usr1 = User(
                email="jfranco@gmail.com",
                password="pwd",
                first_name="James",
                last_name="Franco"
            )
            self.usr2 = User(
                email="mr305@worldwide.mr",
                password="yatusabes",
                first_name="Pitbull",
                last_name="Mister Worldwide"
            )
            self.usr3 = User(**self.usr1.to_dict())
            storage.save()

        @classmethod
        def tearDown(self):
            """ cleanup method to be performed following each test """
            del self.usr1
            del self.usr2
            del self.usr3
            try:
                os.remove("file.json")
            except IOError:
                pass

        def test_doc_string(self):
            """ tests module docstring """
            self.assertTrue(len(User.__doc__) > 0)

        def test_pycodestyle(self):
            """ tests module pycodestyle formatting standard compliance """
            style = pycodestyle.StyleGuide(quiet=True)
            self.assertEqual(
                style.check_files(['models/user.py']).total_errors,
                0,
                "Found code style errors (and warnings)."
            )

        def test_class_attribute_initialization(self):
            """ verifies attributes initialized with correct value & type """
            self.assertEqual(type(self.usr1.email), str)
            self.assertEqual(type(self.usr1.password), str)
            self.assertEqual(type(self.usr1.first_name), str)
            self.assertEqual(type(self.usr1.last_name), str)
            self.assertEqual(type(self.usr2.email), str)
            self.assertEqual(type(self.usr2.password), str)
            self.assertEqual(type(self.usr2.first_name), str)
            self.assertEqual(type(self.usr2.last_name), str)
            self.assertEqual(type(self.usr3.email), str)
            self.assertEqual(type(self.usr3.password), str)
            self.assertEqual(type(self.usr3.first_name), str)
            self.assertEqual(type(self.usr3.last_name), str)
            self.assertEqual(self.usr1.email, "jfranco@gmail.com")
            self.assertEqual(self.usr1.password, "pwd")
            self.assertEqual(self.usr1.first_name, "James")
            self.assertEqual(self.usr1.last_name, "Franco")
            self.assertEqual(self.usr2.email, "mr305@worldwide.mr")
            self.assertEqual(self.usr2.password, "yatusabes")
            self.assertEqual(self.usr2.first_name, "Pitbull")
            self.assertEqual(self.usr2.last_name, "Mister Worldwide")
            self.assertEqual(self.usr3.email, "jfranco@gmail.com")
            self.assertEqual(self.usr3.password, "pwd")
            self.assertEqual(self.usr3.first_name, "James")
            self.assertEqual(self.usr3.last_name, "Franco")


if __name__ == "__main__":
    unittest.main()
