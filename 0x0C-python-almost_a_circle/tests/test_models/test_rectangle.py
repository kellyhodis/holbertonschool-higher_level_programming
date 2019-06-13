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

        # check that id increments with instances
        s = Rectangle(2, 4)
        self.assertEqual(s.id, 2)
        t = Rectangle(3, 3)
        self.assertEqual(t.id, 3)

        # check that id can be assigned
        u = Rectangle(5, 6, id=50)
        self.assertEqual(u.id, 50)
