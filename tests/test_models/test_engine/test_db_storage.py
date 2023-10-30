#!/usr/bin/python3
""" """
import unittest
from models.engine.db_storage import DBStorage


class Test_DatabaseStorage(unittest.TestCase):
    """ tests for DBStorage """
    def test_all(self):
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
