#!/usr/bin/python3
""" """
import os
import MySQLdb
import unittest
import subprocess
import pycodestyle
from models import storage
from models.city import City


class Test_City(unittest.TestCase):
    """ """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        def test_state_id_db(self):
            """ """
            command = [
                "bash",
                "-c",
                "cat setup_mysql_dev.sql | mysql -hlocalhost -uroot"
            ]
            subprocess.run(command, capture_output=True, text=True)
            db = MySQLdb.connect(
                host="localhost",
                user="hbnb_dev",
                passwd="hbnb_dev_pwd",
                db="hbnb_dev_db"
            )
            cursor = db.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS states (name VARCHAR(255))"
            )
            cursor.execute(
                "SELECT COUNT(*) FROM states"
            )
            result_before = cursor.fetchone()[0]
            subprocess.call([
                'echo', 'create State name=\"California\"', '|',
                'HBNB_MYSQL_USER=hbnb_dev',
                'HBNB_MYSQL_PWD=hbnb_dev_pwd',
                'HBNB_MYSQL_HOST=localhost',
                'HBNB_MYSQL_DB=hbnb_dev_db',
                'HBNB_TYPE_STORAGE=db',
                './console.py'
            ])
            cursor.execute("SELECT COUNT(*) FROM states")
            result_after = cursor.fetchone()[0]
            count = result_after - result_before
            self.assertEqual(result_after - result_before, count)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
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
