#!/usr/bin/python3
""" base_model tests """
import os
import unittest
# import datetime
import pycodestyle
from models import storage
from genericpath import exists
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """ BaseModel __init__ method tests """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.mod1 = BaseModel()
        self.mod2 = BaseModel()
        self.mod3 = BaseModel(**self.mod1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.mod1
        del self.mod2
        del self.mod3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests docstrings for module, class, & class methods """
        self.assertTrue(len(BaseModel.__doc__) > 0)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)
        self.assertTrue(len(BaseModel.delete.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/base_model.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_id_initialization(self):
        """ verifies id attribute initialized with correct value & type """
        self.assertTrue(self.mod1.id, exists)
        self.assertTrue(self.mod2.id, exists)
        self.assertTrue(type(self.mod1.id) is str)
        self.assertTrue(type(self.mod2.id) is str)
        self.assertEqual(len(self.mod1.id), 36)
        self.assertEqual(len(self.mod2.id), 36)
        self.assertNotEqual(self.mod1.id, self.mod2.id)

    def test_created_at_initialization(self):
        """ verifies created_at attribute initialized correctly """
        self.assertTrue(self.mod1.created_at, exists)
        self.assertTrue(self.mod2.created_at, exists)
        self.assertNotEqual(self.mod1.created_at, self.mod2.created_at)

    def test_updated_at_initialization(self):
        """ verifies updated_at attribute initialized correctly """
        self.assertTrue(self.mod1.updated_at, exists)
        self.assertTrue(self.mod2.updated_at, exists)
        self.assertEqual(self.mod1.created_at, self.mod1.updated_at)
        self.assertEqual(self.mod2.created_at, self.mod2.updated_at)
        self.assertNotEqual(self.mod1.updated_at, self.mod2.updated_at)

    def test_init_kwargs_direct(self):
        """ verifies acceptance of kwargs arguments upon instantiation """
        kwargs_model = BaseModel(id=2147483647)
        self.assertEqual(kwargs_model.id, 2147483647)

    def test_init_kwargs_from_dict(self):
        """ verifies correct instantiation w/ dict supplied as kwargs arg """
        self.assertEqual(self.mod3.id, self.mod1.id)
        self.assertEqual(self.mod3.created_at, self.mod1.created_at)
        self.assertEqual(self.mod3.updated_at, self.mod1.updated_at)
        self.assertEqual(self.mod3.__class__, self.mod1.__class__)

    def test_init_args(self):
        """ verifies that random arguments as args are not recorded """
        args_model = BaseModel([2, 4, 8, 16])
        self.assertNotIn('[2, 4, 8, 16]', args_model.__dict__.items())

    def test_type(self):
        """ verifies that type returns correct object type """
        self.assertTrue(type(self.mod1) is BaseModel)


class TestBaseModel_str(unittest.TestCase):
    """ BaseModel __str__ method tests """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.mod1 = BaseModel()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.mod1

    def test_base_model_str(self):
        """ verifies correct object string representation """
        self.assertEqual(
            str(self.mod1),
            "[{}] ({}) {}".format(
                self.mod1.__class__.__name__,
                self.mod1.id,
                self.mod1.__dict__,
            )
        )
        self.assertEqual(
            self.mod1.__str__(),
            "[{}] ({}) {}".format(
                self.mod1.__class__.__name__,
                self.mod1.id,
                self.mod1.__dict__,
            )
        )


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage inactive'
)
class TestBaseModel_save(unittest.TestCase):
    """ BaseModel save method tests """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.mod1 = BaseModel()
        self.mod1.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.mod1

    def test_save_with_argument(self):
        """ verifies save method raises TypeError when argument supplied """
        with self.assertRaises(TypeError):
            self.mod1.save(1)

    def test_save(self):
        """ tests BaseModel save method correct operation """
        self.assertNotEqual(self.mod1.updated_at, self.mod1.created_at)
        self.assertTrue(self.mod1.created_at < self.mod1.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """ BaseModel to_dict method tests """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.mod1 = BaseModel()
        self.mod1_dict = self.mod1.to_dict()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.mod1

    def test_to_dict_with_argument(self):
        """ verifies to_dict method raises TypeError when arg supplied """
        with self.assertRaises(TypeError):
            self.mod1.to_dict(1)

    def test_to_dict_success(self):
        """ verified that object dictionary initialized & of dict type """
        self.assertTrue(self.mod1_dict, exists)
        self.assertTrue(type(self.mod1_dict) is dict)

    def test_to_dict_keys(self):
        """ verifies to_dict correctly collects obj attributes into keys """
        self.assertIn(
            '__class__',
            self.mod1_dict
        )
        self.assertIn(
            'created_at',
            self.mod1_dict
        )
        self.assertIn(
            'updated_at',
            self.mod1_dict
        )
        self.assertIn(
            'id',
            self.mod1_dict
        )

    def test_to_dict_values(self):
        """ verifies to_dict match attribute values to correct dict keys """
        self.assertEqual(
            self.mod1_dict['__class__'],
            'BaseModel'
        )
        self.assertEqual(
            self.mod1_dict['__class__'],
            self.mod1.__class__.__name__
        )
        self.assertEqual(
            self.mod1_dict['created_at'],
            self.mod1.created_at.isoformat()
        )
        self.assertEqual(
            self.mod1_dict['updated_at'],
            self.mod1.updated_at.isoformat()
        )
        self.assertEqual(self.mod1_dict['id'], self.mod1.id)


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage inactive'
)
class TestBaseModel_delete(unittest. TestCase):
    """ BaseModel delete tests """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.mod1 = BaseModel()
        self.mod1.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.mod1

    def test_delete(self):
        """ tests BaseModel delete method correct operation """
        mod1_id = f'{self.mod1.__class__.__name__}.{self.mod1.id}'
        self.assertIn(mod1_id, storage._FileStorage__objects)
        self.assertIn(self.mod1, storage._FileStorage__objects.values())
        self.mod1.delete()
        self.assertNotIn(mod1_id, storage._FileStorage__objects)
        self.assertNotIn(mod1_id, storage._FileStorage__objects)


# class Test_BaseModel(unittest.TestCase):
#     """ Tests for BaseModel """
#     def __init__(self, *args, **kwargs):
#         """ instantiation """
#         super().__init__(*args, **kwargs)
#         self.name = 'BaseModel'
#         self.value = BaseModel

#     def setUp(self):
#         """ preparation method before each test"""
#         pass

#     def tearDown(self):
#         """ cleanup method following each test """
#         try:
#             os.remove('file.json')
#         except IOError:
#             pass

#     def test_default(self):
#         """ tests type """
#         i = self.value()
#         self.assertEqual(type(i), self.value)

#     def test_kwargs(self):
#         """ tests kwargs as input argument """
#         i = self.value()
#         copy = i.to_dict()
#         new = BaseModel(**copy)
#         self.assertFalse(new is i)

#     def test_kwargs_int(self):
#         """ tests that kwargs int argument raises TypeError """
#         i = self.value()
#         copy = i.to_dict()
#         copy.update({1: 2})
#         with self.assertRaises(TypeError):
#             BaseModel(**copy)

#     def test_todict(self):
#         """ tests to_dict method """
#         i = self.value()
#         n = i.to_dict()
#         self.assertEqual(i.to_dict(), n)

#     def test_kwargs_none(self):
#         """ tests kwargs argument with NoneType key """
#         n = {None: None}
#         with self.assertRaises(TypeError):
#             self.value(**n)

#     def test_kwargs_one(self):
#         """ tests kwargs argument with 1 key """
#         n = {'Name': 'test'}
#         new = self.value(**n)
#         self.assertTrue(isinstance(new, BaseModel))

#     def test_id(self):
#         """ tests id attribute """
#         new = self.value()
#         self.assertEqual(type(new.id), str)

#     def test_created_at(self):
#         """ tests created_at attribute """
#         new = self.value()
#         self.assertEqual(type(new.created_at), datetime.datetime)

#     def test_updated_at(self):
#         """ tests updated_at attribute """
#         new = self.value()
#         self.assertEqual(type(new.updated_at), datetime.datetime)
#         n = new.to_dict()
#         new = BaseModel(**n)
#         self.assertTrue(new.created_at == new.updated_at)


if __name__ == "__main__":
    unittest.main()
