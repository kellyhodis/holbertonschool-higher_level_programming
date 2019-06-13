#!/usr/bin.python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unitest class
    """
    def test___init(self):
        """test for correct instance assignments
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
