#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo



class TestEcho(unittest.TestCase):
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

    def test_parser(self):
        """Checks if parser recognizes a given argument flag."""
        parser = echo.create_parser()
        args_list = ['-ult', 'hello']
        result = parser.parse_args(args_list)
        self.assertTrue(result.upper)
        self.assertTrue(result.lower)
        self.assertTrue(result.title)
        self.assertEqual(result.text, 'hello')

    def test_upper(self):
        """Should uppercase the input text and return the text."""
        args_list = ['-u', 'hello']
        self.assertEqual(echo.main(args_list), 'HELLO')

    def test_upper_long(self):
        """Should uppercase the input text and return the text."""
        args_list = ['--upper', 'hello']
        self.assertEqual(echo.main(args_list), 'HELLO')

    def test_lower(self):
        """Should lowercase the input text and return the text."""
        args_list = ['-l', 'HEllO']
        self.assertEqual(echo.main(args_list), 'hello')

    def test_lower_long(self):
        """Should lowercase the input text and return the text."""
        args_list = ['--lower', 'HEllO']
        self.assertEqual(echo.main(args_list), 'hello')

    def test_title(self):
        """Should titlecase the input text and return the text."""
        args_list = ['-t', 'hello']
        self.assertEqual(echo.main(args_list), 'Hello')

    def test_title_long(self):
        """Should titlecase the input text and return the text."""
        args_list = ['--title', 'hello']
        self.assertEqual(echo.main(args_list), 'Hello')

    def test_all(self):
        """Should return text manipulated based on last flag as defined in parser."""
        args_list = ['-tlu', 'hELlo']
        self.assertEqual(echo.main(args_list), 'Hello')
    
    def test_none(self):
        """Should return unmanipulated text if no arguments are given."""
        args_list = ['piero']
        self.assertEqual(echo.main(args_list), 'piero')


if __name__ == '__main__':
    unittest.main()
