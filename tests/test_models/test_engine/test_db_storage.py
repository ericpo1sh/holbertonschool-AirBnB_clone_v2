#!/usr/bin/python3
""" db_storage tests """
import unittest
import pycodestyle
# from models import storage
# from models.city import City
# from models.state import State
# from sqlalchemy.engine.base import Engine
# from sqlalchemy.orm.session import Session
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

    # def test_class_attributes_private(self):
    #     """ tests attributes of correct types & private status """
    #     self.assertEqual(type(storage._DBStorage__engine), Engine)
    #     self.assertEqual(type(storage._DBStorage__session), Session)
    #     with self.assertRaises(AttributeError):
    #         print(storage.__engine)
    #         print(storage.__session)

    def test_type(self):
        """ verifies that type returns correct object type """
        db = DBStorage()
        self.assertTrue(type(db) is DBStorage)


# class Test_DatabaseStorage(unittest.TestCase):
#     """ tests for DBStorage """
#     @unittest.skipIf(type(storage) is not DBStorage, "skip")
#     @classmethod
#     def setUp(self):
#         """ preparation method to be performed before each test """
#         self.db = DBStorage()
#         self.db.reload()
#         self.state = State(name="Pennsylvania")
#         self.db.new(self.state)
#         self.city = City(name="Philadelphia", state_id=self.state.id)
#         self.db.new(self.city)
#         self.db.save()

#     @unittest.skipIf(type(storage) is not DBStorage, "skip")
#     @classmethod
#     def tearDown(self):
#         """ cleanup method to be performed following each test """
#         self.db.delete(self.state)
#         self.db.delete(self.city)
#         self.db.save()
#         self.db.close()
#         del self.db

#     @unittest.skipIf(type(storage) is not DBStorage, "skip")
#     def test_all(self):
#         """ tests DBStorage all method correct operation """
#         obj_dict = self.db.all()
#         self.assertEqual(type(obj_dict), dict)
#         city_dict = self.db.all(City)
#         self.assertEqual(type(city_dict), dict)

#     @unittest.skipIf(type(storage) is not DBStorage, "skip")
#     def test_new(self):
#         """ tests DBStorage new method correct operation """
#         new_state = State(name="New Jersey")
#         new_state_id = f'{new_state.__class__.__name__}.{new_state.id}'
#         self.db.new(new_state)
#         self.assertIn(new_state_id, self.db.all())
#         self.assertIn("New Jersey", self.db.all(State).values())

#     @unittest.skipIf(type(storage) is not DBStorage, "skip")
#     def test_save(self):
#         """ tests DBStorage save method """
#         save_city = City(name="Upper Darby", state_id=self.state.id)
#         save_city_id = (
#             f'{self.save_city.__class__.__name__}.{self.save_city.id}'
#         )
#         self.assertNotIn(
#             save_city_id,
#             self.db.all()
#         )
#         self.db.new(save_city)
#         self.db.save()
#         self.assertIn(
#             save_city_id,
#             self.db.all()
#         )
#         self.assertIn(
#             "Upper Darby",
#             self.db.all(City).values()
#         )

#     @unittest.skipIf(type(storage) is not DBStorage, "skip")
#     def test_delete(self):
#         """ tests delete method correct operation """
#         goodbye = State(name="Florida")
#         goodbye_id = f'{self.goodbye.__class__.__name__}.{self.goodbye.id}'
#         self.assertIn(
#             goodbye_id,
#             self.db.all()
#         )
#         self.db.new(goodbye)
#         self.db.save()
#         self.db.delete(goodbye)
#         self.assertNotIn(
#             goodbye_id,
#             self.db.all()
#         )

#     @unittest.skipIf(type(storage) is not DBStorage, "skip")
#     def test_reload(self):
#         """ tests DBStorage reload method correct operation """
#         before = self.db._DBStorage__session
#         self.db.reload()
#         self.assertNotEqual(before, self.db._DBStorage__session)


if __name__ == "__main__":
    unittest.main()
