#!/usr/bin/python3
""" """
import io
import sys
import unittest
from console import HBNBCommand


class Test_Console(unittest.TestCase):
    """ tests for console """
    def test_create_instance(self):
        """ """
        output = io.StringIO()
        sys.stdout = output
        console = HBNBCommand()
        console.onecmd(
            "create User email=\"test\" password=\"kittycat\" id=\"12\""
        )
        sys.stdout = sys.__stdout__
        expected_output = output.getvalue()
        self.assertIn('12', expected_output)


if __name__ == "__main__":
    unittest.main()
