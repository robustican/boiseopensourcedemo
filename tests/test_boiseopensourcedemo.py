#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_boiseopensourcedemo
----------------------------------

Tests for `boiseopensourcedemo` module.
"""

import unittest

from boiseopensourcedemo import boiseopensourcedemo


class TestBoiseopensourcedemo(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertEquals(boiseopensourcedemo.a_cool_method(5), 25)

    def test_something_else(self):
        self.assertRaises(NotImplementedError, boiseopensourcedemo.a_cool_method, 1.1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()