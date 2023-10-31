#!/usr/bin/python3
""" place tests """
import os
import unittest
import pycodestyle
from models import storage
from models.place import Place
from models.base_model import BaseModel, Base


class Test_Place(unittest.TestCase):
    """ tests for Place subclass of BaseModel """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.place1 = Place(
            user_id="ericdude",
            name="Eric",
            description="test",
            number_rooms=1,
            number_bathrooms=1,
            max_guest=1,
            price_by_night=1,
            latitude=11.11,
            longitude=11.11,
            amenity_ids=["water", "test"]
        )
        self.place2 = Place(
            user_id="sammydude",
            name="Sammy",
            description="testing",
            number_rooms=2,
            number_bathrooms=2,
            max_guest=2,
            price_by_night=2,
            latitude=22.22,
            longitude=22.22,
            amenity_ids=["water", "food"]
        )
        self.place3 = Place(**self.place1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.place1
        del self.place2
        del self.place3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests module docstring """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/place.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        """ verifies attributes initialized with correct value & type """
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)
        self.assertEqual(type(self.place2.user_id), str)
        self.assertEqual(type(self.place2.name), str)
        self.assertEqual(type(self.place2.description), str)
        self.assertEqual(type(self.place2.number_rooms), int)
        self.assertEqual(type(self.place2.number_bathrooms), int)
        self.assertEqual(type(self.place2.max_guest), int)
        self.assertEqual(type(self.place2.price_by_night), int)
        self.assertEqual(type(self.place2.latitude), float)
        self.assertEqual(type(self.place2.longitude), float)
        self.assertEqual(type(self.place2.amenity_ids), list)
        self.assertEqual(type(self.place3.user_id), str)
        self.assertEqual(type(self.place3.name), str)
        self.assertEqual(type(self.place3.description), str)
        self.assertEqual(type(self.place3.number_rooms), int)
        self.assertEqual(type(self.place3.number_bathrooms), int)
        self.assertEqual(type(self.place3.max_guest), int)
        self.assertEqual(type(self.place3.price_by_night), int)
        self.assertEqual(type(self.place3.latitude), float)
        self.assertEqual(type(self.place3.longitude), float)
        self.assertEqual(type(self.place3.amenity_ids), list)
        self.assertEqual(self.place1.user_id, "ericdude")
        self.assertEqual(self.place1.name, "Eric")
        self.assertEqual(self.place1.description, "test")
        self.assertEqual(self.place1.number_rooms, 1)
        self.assertEqual(self.place1.number_bathrooms, 1)
        self.assertEqual(self.place1.max_guest, 1)
        self.assertEqual(self.place1.price_by_night, 1)
        self.assertEqual(self.place1.latitude, 11.11)
        self.assertEqual(self.place1.longitude, 11.11)
        self.assertEqual(self.place1.amenity_ids, ["water", "test"])
        self.assertEqual(self.place2.user_id, "sammydude")
        self.assertEqual(self.place2.name, "Sammy")
        self.assertEqual(self.place2.description, "testing")
        self.assertEqual(self.place2.number_rooms, 2)
        self.assertEqual(self.place2.number_bathrooms, 2)
        self.assertEqual(self.place2.max_guest, 2)
        self.assertEqual(self.place2.price_by_night, 2)
        self.assertEqual(self.place2.latitude, 22.22)
        self.assertEqual(self.place2.longitude, 22.22)
        self.assertEqual(self.place2.amenity_ids, ["water", "food"])
        self.assertEqual(self.place3.user_id, "ericdude")
        self.assertEqual(self.place3.name, "Eric")
        self.assertEqual(self.place3.description, "test")
        self.assertEqual(self.place3.number_rooms, 1)
        self.assertEqual(self.place3.number_bathrooms, 1)
        self.assertEqual(self.place3.max_guest, 1)
        self.assertEqual(self.place3.price_by_night, 1)
        self.assertEqual(self.place3.latitude, 11.11)
        self.assertEqual(self.place3.longitude, 11.11)
        self.assertEqual(self.place3.amenity_ids, ["water", "test"])

    def test_type_subclass(self):
        """ tests correct type/subclass heirarchy """
        self.assertEqual(type(self.place1), Place)
        self.assertTrue(isinstance(self.place1, Place))
        self.assertTrue(issubclass(self.place1.__class__, BaseModel))
        self.assertTrue(issubclass(self.place1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
