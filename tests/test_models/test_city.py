#!/usr/bin/python3
""" """
import MySQLdb
import subprocess
from os import getenv
from models.city import City
from tests.test_models.test_base_model import Test_BaseModel


class Test_City(Test_BaseModel):
    """ """
    if getenv("HBNB_TYPE_STORAGE") == "db":
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

    if getenv("HBNB_TYPE_STORAGE") != "db":
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
