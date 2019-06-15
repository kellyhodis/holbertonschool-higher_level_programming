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

        # check that size must be >= 0
        with self.assertRaises(ValueError):
            v = Square(-1)

        with self.assertRaises(ValueError):
            u = Square(0)

        # check that size must be an integer
        with self.assertRaises(TypeError):
            w = Square("1")

        # check that x must be an integer
        with self.assertRaises(TypeError):
            z = Square(1, "1")

        # check that x must be >= 0
        with self.assertRaises(ValueError):
            c = Square(1, -1)

        # check that y must be >= 0
        with self.assertRaises(ValueError):
            d = Square(1, 1, -1)

        # check that y must be an integer
        with self.assertRaises(TypeError):
            a = Square(1, 1, "1")

        # check that assignments are correct
        b = Square(1, 1, 1, 1)
        self.assertEqual(b.width, 1)
        self.assertEqual(b.height, 1)
        self.assertEqual(b.x, 1)
        self.assertEqual(b.y, 1)
        self.assertEqual(b.id, 1)

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

    def test_square_save_to_file(self):
        """test for save_to_file with Square
        """
        s = Square(3)

        l = []
        l.append(s)
        s.save_to_file(l)

        # test that file is not empty
        with open('Square.json') as file:
            self.assertTrue(file.read(1))

        # test saving empty list to file
        p = []
        s.save_to_file(p)

        with open('Square.json') as file:
            self.assertTrue(file.read(1))

    def test_square_load_from_file(self):
        """test for load_from_file with Square
        """
        s = Square(2)

        # check when file doesn't exist
        l = s.load_from_file()

        self.assertIsInstance(l, list)

        # check when file does exist
        li = []
        li.append(s)
        s.save_to_file(li)
        l = s.load_from_file()
        self.assertIsInstance(l, list)
