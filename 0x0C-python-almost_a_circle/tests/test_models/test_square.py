#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """unittest class
    """
    def test___init(self):
        """test for __init__ method
        """
        # check for correct instance assignments
        r = Square(1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test___str(self):
        """test for __str__ method
        """
        r = Square(3)

        # check that metho returns obj of type string
        R = r.__str__
        self.assertTrue(R, str)

    def test_update(self):
        """test for update method
        """
        r = Square(1)

        # check that every value is updated with list
        r.update(3, 3, 2, 1)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

        # check that every value is updated with dictionary
        dict = {"id": 1, "size": 2, "x": 0, "y": 1}
        r.update(**dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 1)

    def test_to_dictionary(self):
        """test for to_dictionary method
        """
        r = Square(3)

        # check that method returns obj of type dictionary
        R = r.to_dictionary()
        self.assertIsInstance(R, dict)

    def test_size_property_and_setter(self):
        """test for size property and setter
        """
        r = Square.create()
        with self.assertRaises(TypeError):
            r.size = "r"

    def test_square_load_from_file(self):
        """test for load_from_file with Square
        """
        s = Square(2)

        # check when file doesn't exist
        l = s.load_from_file()
        self.assertIsInstance(l, list)
