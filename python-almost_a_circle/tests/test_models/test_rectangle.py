#!/usr/bin/python3
"""unittest for the Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test functions for the Rectangle class"""

    def test_instantiaton_without_args(self):
        """
        Creating a Rectangle instance with no arguments
        fails with a TypeError exception
        """
        self.assertRaises(TypeError, Rectangle)

    def test_instatiation_with_two_args(self):
        """
        Creating a Rectangle instance with two arguments
        succeeds with width set to the first argument
        and height set to the second argument
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_instatiation_with_three_args(self):
        """
        Creating a Rectangle instance with three arguments
        succeeds with width set to the first argument,
        height set to the second argument and x set to the
        third argument
        """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_instatiation_with_four_args(self):
        """
        Creating a Rectangle instance with four arguments
        succeeds with width set to the first argument,
        height set to the second argument, x set to the
        third argument and y set to the fourth argument
        """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_instatiation_with_five_args(self):
        """
        Creating a Rectangle instance with five arguments
        succeeds with width set to the first argument,
        height set to the second argument, x set to the
        third argument, y to the fourth argument and id
        set to the fifth argument
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_instantiation_with_first_arg_string(self):
        """Test that instatiating a Rectangle class fails
        when the first argument is not an integer
        """
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_instantiation_with_second_arg_string(self):
        """Test that instatiating a Rectangle class fails
        when second argument is not an integer
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_instantiation_with_third_arg_string(self):
        """Test that instatiating a Rectangle class fails
        when third argument is not an integer
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")
