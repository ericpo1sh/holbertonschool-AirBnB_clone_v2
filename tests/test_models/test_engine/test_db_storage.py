#!/usr/bin/python3
""" """
import unittest
import pycodestyle
from models import storage
from models.engine.db_storage import DBStorage


class TestDBStorage_class(unittest.TestCase):
    """ tests DBStorage class init & formatting related operations """
    def test_doc_string(self):
        """ tests docstrings for module, class, & class methods """
        self.assertTrue(len(DBStorage.__doc__) > 0)
        self.assertTrue(len(DBStorage.all.__doc__) > 0)
        self.assertTrue(len(DBStorage.new.__doc__) > 0)
        self.assertTrue(len(DBStorage.save.__doc__) > 0)
        self.assertTrue(len(DBStorage.reload.__doc__) > 0)
        self.assertTrue(len(DBStorage.delete.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/engine/file_storage.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_call_with_argument(self):
        """ verifies that TypeError raised when argument supplied """
        with self.assertRaises(TypeError):
            DBStorage(1)

    def test_class_attributes_private(self):
        """ tests attributes of correct types & private status """
        self.assertTrue(type(storage._FileStorage__file_path) is str)
        self.assertTrue(type(storage._FileStorage__objects) is dict)
        with self.assertRaises(AttributeError):
            print(storage.__objects)
            print(storage.__file_path)

    def test_type(self):
        """ verifies that type returns correct object type """
        storage = DBStorage()
        self.assertTrue(type(storage) is DBStorage)


class Test_DatabaseStorage(unittest.TestCase):
    """ tests for DBStorage """
    def test_tipo(self):
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)


if __name__ == "__main__":
    unittest.main()
