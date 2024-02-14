#!/usr/bin/python3
"""unittest for the Rectangle class"""

import unittest
from io import StringIO
import sys
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

    def test_instantiation_with_fourth_arg_string(self):
        """Test that instatiating a Rectangle class fails
        when fourth argument is not an integer
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_instantiation_with_first_arg_negative(self):
        """Test that instatiating a Rectangle class fails
        when first argument is negative
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_instantiation_with_second_arg_negative(self):
        """Test that instatiating a Rectangle class fails
        when second argument is negative
        """
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_instantiation_with_first_arg_zero(self):
        """Test that instatiating a Rectangle class fails
        when first argument is zero
        """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_instantiation_with_second_arg_zero(self):
        """Test that instatiating a Rectangle class fails
        when second argument is zero
        """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_instantiation_with_third_arg_negative(self):
        """Test that instatiating a Rectangle class fails
        when third argument is negative
        """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_instantiation_with_fourth_arg_negative(self):
        """Test that instatiating a Rectangle class fails
        when fourth argument is negative
        """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_method_area_exists(self):
        """Test that area method exists on rectangle instance"""
        r = Rectangle(2, 3)
        self.assertTrue(hasattr(r, "area"))
        self.assertEqual(r.area(), 6)

    def test_printable(self):
        """Tests that the instance can be stringified
        """
        r = Rectangle(2, 3, 0, 0, 25)
        self.assertEqual(r.__str__(), "[Rectangle] (25) 0/0 - 2/3")

    def test_display_without_x_and_y(self):
        """Tests that display method when called without for
        a instantiated without x and y produces correct output
        """
        r = Rectangle(3, 3)
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "###\n###\n###\n")

    def test_display_x_offset_only(self):
        """Tests that the graphical representation prints out correctly with x offset
        """
        r = Rectangle(2, 2, 1)
        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        r.display()                     # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), " ##\n ##\n")

    def test_to_dictionary_method(self):
        """Tests that when called, to_dictionary method
        returns the correct value"""
        r = Rectangle(2, 3, 0, 0, 35)
        d = r.to_dictionary()
        self.assertEqual(
            d, {'x': 0, 'y': 0, 'id': 35, 'height': 3, 'width': 2})
