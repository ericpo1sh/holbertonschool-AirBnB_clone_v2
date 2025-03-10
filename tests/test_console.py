#!/usr/bin/python3
""" console tests """
import os
import unittest
import pycodestyle
from console import HBNBCommand, signal_thing


class TestConsole_class(unittest.TestCase):
    """ tests console class init & formatting related operations """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.konsol = HBNBCommand()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        try:
            os.remove("file.json")
        except IOError:
            pass
        del self.konsol

    def test_doc_string(self):
        """ tests docstrings for module, class, & class methods """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.preloop.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.precmd.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.postcmd.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_quit.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_quit.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_EOF.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.emptyline.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_create.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_create.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_show.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_show.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_destroy.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_all.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_all.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_count.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_count.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_update.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.help_update.__doc__) > 0)
        self.assertTrue(len(HBNBCommand.do_clear.__doc__) > 0)
        self.assertTrue(len(signal_thing.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['console.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_type(self):
        """ verifies that type returns correct object type """
        konsol = HBNBCommand()
        self.assertEqual(type(konsol), HBNBCommand)
        self.assertTrue(isinstance(konsol, HBNBCommand))


if __name__ == "__main__":
    unittest.main()
