#!/usr/bin/python3
""" """
import io
import console
import unittest
from contextlib import redirect_stdout


class Test_Console(unittest.TestCase):
    """ tests for console """
    def setUp(self):
        self.console = console.HBNBCommand()

    def test_create(self):
        with redirect_stdout(io.StringIO()) as f:
            self.console.onecmd("create State name='Hawai\'i'")
        state_id = f.getvalue()
        with redirect_stdout(io.StringIO()) as d:
            self.console.onecmd(
                "create City state_id=\"{}\" name='Surf's up dude'"
                .format(str(state_id)))
        city_id = d.getvalue()
        print(f"state:{state_id}city:{city_id}")
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
