#!/usr/bin/python3
""" db_storage tests """
import os
import unittest
import pycodestyle
from models import storage
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.getenv("HBNB_ENV") != "db", 'DBStorage inactive')
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
            style.check_files(['models/engine/db_storage.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_call_with_argument(self):
        """ verifies that TypeError raised when argument supplied """
        with self.assertRaises(TypeError):
            DBStorage(1)

    def test_class_attributes_private(self):
        """ tests attributes of correct types & private status """
        self.assertEqual(type(storage._DBStorage__engine), Engine)
        self.assertEqual(type(storage._DBStorage__session), Session)
        with self.assertRaises(AttributeError):
            print(storage.__engine)
            print(storage.__session)

    def test_type(self):
        """ verifies that type returns correct object type """
        db = DBStorage()
        self.assertTrue(type(db) is DBStorage)


if __name__ == "__main__":
    unittest.main()
