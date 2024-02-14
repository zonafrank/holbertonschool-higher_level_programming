#!/usr/bin/python3
"""unittest for the Square class"""

import unittest
from io import StringIO
import sys
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test functions for the Square class"""

    def test_instantiaton_without_args(self):
        """
        Creating a Square instance with no arguments
        fails with a TypeError exception
        """
        self.assertRaises(TypeError, Square)

    def test_instatiation_with_two_args(self):
        """
        Creating a Square instance with two arguments
        succeeds with width set to the first argument
        and height set to the second argument
        """
        r = Square(1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)

    def test_instatiation_with_three_args(self):
        """
        Creating a Square instance with three arguments
        succeeds with width set to the first argument,
        height set to the second argument and x set to the
        third argument
        """
        r = Square(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_instatiation_with_four_args(self):
        """
        Creating a Square instance with four arguments
        succeeds with width set to the first argument,
        height set to the second argument, x set to the
        third argument and y set to the fourth argument
        """
        r = Square(1, 2, 3, 45)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 45)

    def test_instantiation_with_first_arg_string(self):
        """Test that instatiating a Square class fails
        when the first argument is not an integer
        """
        with self.assertRaises(TypeError):
            r = Square("1")

    def test_instantiation_with_second_arg_string(self):
        """Test that instatiating a Square class fails
        when second argument is not an integer
        """
        with self.assertRaises(TypeError):
            r = Square(1, "2")

    def test_instantiation_with_third_arg_string(self):
        """Test that instatiating a Square class fails
        when third argument is not an integer
        """
        with self.assertRaises(TypeError):
            r = Square(1, 2, "3")

    def test_instantiation_with_first_arg_negative(self):
        """Test that instatiating a Square class fails
        when first argument is negative
        """
        with self.assertRaises(ValueError):
            r = Square(-1)

    def test_instantiation_with_second_arg_negative(self):
        """Test that instatiating a Square class fails
        when second argument is negative
        """
        with self.assertRaises(ValueError):
            r = Square(1, -2)

    def test_instantiation_with_first_arg_zero(self):
        """Test that instatiating a Square class fails
        when first argument is zero
        """
        with self.assertRaises(ValueError):
            r = Square(0)

    def test_instantiation_with_second_arg_negative(self):
        """Test that instatiating a Square class fails
        when third argument is negative
        """
        with self.assertRaises(ValueError):
            r = Square(1, -2)

    def test_instantiation_with_third_arg_negative(self):
        """Test that instatiating a Square class fails
        when fourth argument is negative
        """
        with self.assertRaises(ValueError):
            r = Square(1, 2, -3)

    def test_method_area_exists(self):
        """Test that area method exists on Square instance"""
        r = Square(2)
        self.assertTrue(hasattr(r, "area"))
        self.assertEqual(r.area(), 4)

    def test_printable(self):
        """Tests that the instance can be stringified
        """
        r = Square(2, 0, 0, 25)
        self.assertEqual(r.__str__(), "[Square] (25) 0/0 - 2")

    def test_display_without_x_and_y(self):
        """Tests that display method when called without for
        a instantiated without x and y produces correct output
        """
        r = Square(3)
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "###\n###\n###\n")

    def test_display_x_offset_only(self):
        """Tests that the graphical representation prints out correctly with x offset
        """
        r = Square(2, 1)
        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        r.display()                     # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), " ##\n ##\n")

    def test_to_dictionary_method(self):
        """Tests that when called, to_dictionary method
        returns the correct value"""
        r = Square(2, 0, 0, 35)
        d = r.to_dictionary()
        self.assertEqual(
            d, {'x': 0, 'y': 0, 'id': 35, 'size': 2})

    def test_update_method_with_args(self):
        """Tests that the update method works with args
        """
        r = Square(4, 2, 3)
        r.update(81, 3, 2, 3)
        self.assertEqual(r.id, 81)
        self.assertEqual(r.size, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_update_method_with_kwargs(self):
        """Test that the update method when called with
        kwargs works as expected
        """
        r = Square(2, 1, 1, 55)
        r.update(id=56, size=3, x=2, y=2)
        self.assertEqual(r.id, 56)
        self.assertEqual(r.size, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_parent_create_method(self):
        """Test that the parent create method works
        as expected when called from the child class
        """
        r = Square.create(id=123, size=3, x=3, y=3)
        self.assertEqual(r.id, 123)
        self.assertEqual(r.size, 3)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 3)

    def test_square_save_to_file(self):
        filename = "Square.json"
        if (os.path.isfile(filename)):
            os.remove(filename)

        Square.save_to_file(None)
        content = ""
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        os.remove(filename)
        self.assertEqual(content, "[]")

        Square.save_to_file([])
        content = ""
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        os.remove(filename)
        self.assertEqual(content, "[]")

        Square.save_to_file([Square(2, 0, 0, 99)])
        content = ""
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        os.remove(filename)
        self.assertEqual(
            content,
            '[{"id": 99, "x": 0, "size": 2, "y": 0}]'
        )

    def test_Square_load_from_nonexistent_file(self):
        """Tests that load_from_file class method works
        as expected when file does not exist
        """
        lst = Square.load_from_file()
        self.assertEqual(lst, [])

    def test_Square_load_from_existing_file(self):
        """Tests that load_from_file works when works
        as expected when called with None as argument
        """
        Square.save_to_file(None)
        lst = Square.load_from_file()
        self.assertEqual(lst, [])


if __name__ == "__main__":
    unittest.main()
