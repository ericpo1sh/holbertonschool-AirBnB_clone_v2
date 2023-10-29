#!/usr/bin/python3
""" """
import unittest
from models.engine.db_storage import DBStorage


class Test_DatabaseStorage(unittest.TestCase):
    def test_all(self):
        """ __objects properly returned """
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)
