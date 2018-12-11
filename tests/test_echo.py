#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo

# Your test case class goes here


class TestArgs(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        self.assertEqual(echo.upper('hello'), 'HELLO')

    def test_lower(self):
        self.assertEqual(echo.lower('HEllo'), 'hello')

    def test_title(self):
        self.assertEqual(echo.title('hello'), 'Hello')


if __name__ == '__main__':
    unittest.main()
