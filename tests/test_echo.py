#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here


class TestArgs(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(echo.upper('hello'), 'HELLO')

    def test_lower(self):
        self.assertEqual(echo.lower('HEllo'), 'hello')

    def test_title(self):
        self.assertEqual(echo.title('hello'), 'Hello')


if __name__ == '__main__':
    unittest.main()
