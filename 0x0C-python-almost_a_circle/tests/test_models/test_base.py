#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest class
    """
    def test___init(self):
        """test for __init__ method
        """
        # test the id counter
        s = Base()
        self.assertEqual(s.id, 1)
        t = Base()
        self.assertEqual(t.id, 2)
        s.id = 2
        self.assertEqual(s.id, 2)
