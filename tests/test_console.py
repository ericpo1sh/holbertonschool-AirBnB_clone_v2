#!/usr/bin/python3
""" console tests """
import os
import unittest
import pycodestyle
from io import StringIO
from unittest.mock import patch
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
            style.check_files(['models/engine/file_storage.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_type(self):
        """ verifies that type returns correct object type """
        konsol = HBNBCommand()
        self.assertEqual(type(konsol), HBNBCommand)
        self.assertTrue(isinstance(konsol, HBNBCommand))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_create(self):
        """ test create command operation """
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("create BaseModel")
            base = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("create City")
            city = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("all BaseModel")
            self.assertIn(base, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("all City")
            self.assertIn(city, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd(
                'create City name="Kingston" state_id="00000012"'
            )
            city = file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("all City")
            self.assertIn(city, file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("create")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("create havoc")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())

    def test_show(self):
        """ tests show command operation """
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("show")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("show me_the_money")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("show City")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("show City 2048")
            self.assertEqual("** no instance found **\n", file.getvalue())

    def test_destroy(self):
        """ tests destroy command operation """
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("destroy")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("destroy Camp")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("destroy City")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("destroy City 2048")
            self.assertEqual("** no instance found **\n", file.getvalue())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_all(self):
        """ tests all command operation """
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("all my_friends")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("all City")
            self.assertEqual("[]\n", file.getvalue())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_update(self):
        """Test update command input."""
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("update")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("update your_mom")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("update City")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("update City 2048")
            self.assertEqual("** no instance found **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("all City")
            city = file.getvalue()
        city_id = city[city.find('(')+1:city.find(')')]
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd(f"update City {city_id}")
            self.assertEqual("** attribute name missing **\n", file.getvalue())
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd(f"update City {city_id} hero")
            self.assertEqual("** value missing **\n", file.getvalue())

    def test_help(self):
        """ tests correct operation of help commands """
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help quit")
            self.assertTrue(len(file.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help EOF")
            self.assertTrue(len(file.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help create")
            self.assertTrue(len(file.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help all")
            self.assertTrue(len(file.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help show")
            self.assertTrue(len(file.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help destroy")
            self.assertTrue(len(file.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help count")
            self.assertTrue(len(file.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as file:
            self.konsol.onecmd("help update")
            self.assertTrue(len(file.getvalue()) > 0)

    def test_emptyline(self):
        """ tests correct response upon emptyline"""
        with patch("sys.stdout", new=StringIO()) as file:
            self.konsol.onecmd("\n")
            self.assertEqual("", file.getvalue())


if __name__ == "__main__":
    unittest.main()
