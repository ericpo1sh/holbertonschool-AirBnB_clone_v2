#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
import pycodestyle
from models import storage
from genericpath import exists
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_class(unittest.TestCase):
    """ tests FileStorage class init & formatting related operations """
    def test_doc_string(self):
        """ tests docstrings for module, class, & class methods """
        self.assertTrue(len(FileStorage.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertTrue(len(FileStorage.new.__doc__) > 0)
        self.assertTrue(len(FileStorage.save.__doc__) > 0)
        self.assertTrue(len(FileStorage.reload.__doc__) > 0)

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
            FileStorage(1)

    def test_class_attributes_private(self):
        """ tests attributes of correct types & private status """
        self.assertTrue(type(storage._FileStorage__file_path) is str)
        self.assertTrue(type(storage._FileStorage__objects) is dict)
        with self.assertRaises(AttributeError):
            print(storage.__objects)
            print(storage.__file_path)

    def test_type(self):
        """ verifies that type returns correct object type """
        self.assertTrue(type(storage) is FileStorage)


class TestFileStorage_all(unittest.TestCase):
    """ tests FileStorage all method """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.obj = BaseModel()
        self.obj.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all(self):
        """ tests FileStorage all method correct operation """
        self.assertTrue(self.obj, exists)
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage.all()
        )
        self.assertTrue(type(storage.all()) is dict)
        self.assertTrue(len(storage.all()) > 0)

    # def test_all_with_argument(self):
    #     """ verifies all method raises TypeError when argument supplied """
    #     with self.assertRaises(KeyError):
    #         storage.all(1)


class TestFileStorage_new(unittest.TestCase):
    """ tests FileStorage new method """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.obj = BaseModel()
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_new(self):
        """ tests FileStorage new method correct operation """
        storage.new(self.obj)
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage._FileStorage__objects
        )
        self.assertIn(self.obj, storage.all().values())

    def test_new_excessive_arguments(self):
        """ verifies new method raises TypeError with too many arguments """
        with self.assertRaises(TypeError):
            storage.new(self.obj, 6)

    def test_new_undesired_object_type_argument(self):
        """ verifies new method raises AttributeError with non-obj argument """
        with self.assertRaises(AttributeError):
            storage.new(8)
            storage.new({2, 4, 8})


class TestFileStorage_save(unittest.TestCase):
    """ tests FileStorage save method """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.obj = BaseModel()
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save(self):
        """ tests FileStorage save method correct operation """
        self.obj.save()
        self.assertTrue(os.path.exists('file.json'))
        with open("file.json") as file:
            content = file.read()
            self.assertIn(
                f"{self.obj.__class__.__name__}.{self.obj.id}",
                content
            )
            self.assertTrue(len(content) > 0)

    def test_save_with_argument(self):
        """ verifies save method raises TypeError upon argument supplied """
        with self.assertRaises(TypeError):
            storage.save(1)


class TestFileStorage_reload(unittest.TestCase):
    """ tests FileStorage reload method """
    def test_reload(self):
        """ tests FileStorage reload method correct operation """
        self.obj = BaseModel()
        self.obj.save()
        storage.reload()
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage._FileStorage__objects
        )
        self.assertTrue(len(storage.all()) > 0)
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_reload_with_argument(self):
        """ verifies reload method raises TypeError upon argument supplied """
        with self.assertRaises(TypeError):
            storage.reload(1)


# class Test_FileStorage(unittest.TestCase):
#     """ Class to test the file storage method """
#     def setUp(self):
#         """ Set up test environment """
#         del_list = []
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             for key in storage._FileStorage__objects.keys():
#                 del_list.append(key)
#             for key in del_list:
#                 del storage._FileStorage__objects[key]

#     def tearDown(self):
#         """ Remove storage file at end of tests """
#         try:
#             os.remove('file.json')
#         except IOError:
#             pass

#     def test_obj_list_empty(self):
#         """ __objects is initially empty """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             self.assertEqual(len(storage.all()), 0)

#     def test_new(self):
#         """ New object is correctly added to __objects """
#         BaseModel()
#         temp = None
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             for obj in storage.all().values():
#                 temp = obj
#         self.assertTrue(temp is None)

#     def test_all(self):
#         """ __objects is properly returned """
#         BaseModel()
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             temp = storage.all()
#             self.assertIsInstance(temp, dict)

#     def test_base_model_instantiation(self):
#         """ File is not created on BaseModel save """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             BaseModel()
#             self.assertFalse(os.path.exists('file.json'))

#     def test_empty(self):
#         """ Data is saved to file """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             new = BaseModel()
#             thing = new.to_dict()
#             new.save()
#             BaseModel(**thing)
#             self.assertNotEqual(os.path.getsize('file.json'), 0)

#     def test_save(self):
#         """ FileStorage save method """
#         BaseModel()
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             storage.save()
#             self.assertTrue(os.path.exists('file.json'))

#     def test_reload(self):
#         """ Storage file is successfully loaded to __objects """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             new = BaseModel()
#             storage.save()
#             storage.reload()
#             loaded = None
#             for obj in storage.all().values():
#                 loaded = obj
#             self.assertNotEqual(new, loaded)

#     def test_reload_empty(self):
#         """ Load from an empty file """
#         with open('file.json', 'w'):
#             pass
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             with self.assertRaises(ValueError):
#                 storage.reload()

#     def test_reload_from_nonexistent(self):
#         """ Nothing happens if file does not exist """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             self.assertEqual(storage.reload(), None)

#     def test_base_model_save(self):
#         """ BaseModel save method calls storage save """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             new = BaseModel()
#             new.save()
#             self.assertTrue(os.path.exists('file.json'))

#     def test_type_path(self):
#         """ Confirm __file_path is string """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             self.assertEqual(type(storage._FileStorage__file_path), str)

#     def test_storage_var_created(self):
#         """ FileStorage object storage created """
#         if getenv("HBNB_TYPE_STORAGE") != "db":
#             from models.engine.file_storage import FileStorage
#             print(type(storage))
#             self.assertEqual(type(storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
