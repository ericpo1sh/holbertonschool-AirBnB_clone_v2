#!/usr/bin/python3
""" """
import io
import sys
import unittest
from console import HBNBCommand


class Test(unittest.TestCase):
    def test_create_instance(self):
        """ """
        output = io.StringIO()
        sys.stdout = output
        console = HBNBCommand()
        console.onecmd(
            "create User email=\"test\" password=\"kittycat\" id=\"2\""
        )
        sys.stdout = sys.__stdout__
        expected_output = output.getvalue()
        self.assertIn('2', expected_output)


if __name__ == "__main__":
    unittest.main()
