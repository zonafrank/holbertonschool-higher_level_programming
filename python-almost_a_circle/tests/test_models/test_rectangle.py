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

    def test_update_method_with_args(self):
        """Tests that the update method works with args
        """
        r = Rectangle(4, 5, 2, 3)
        r.update(81, 3, 4, 2, 3)
        self.assertEqual(r.id, 81)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_update_method_with_kwargs(self):
        """Test that the update method when called with
        kwargs works as expected
        """
        r = Rectangle(2, 3, 1, 1, 55)
        r.update(id=56, width=3, height=4, x=2, y=2)
        self.assertEqual(r.id, 56)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_parent_create_method(self):
        """Test that the parent create method works
        as expected when called from the child class
        """
        r = Rectangle.create(id=123, width=3, height=4, x=3, y=3)
        self.assertEqual(r.id, 123)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 3)

    def test_parent_save_to_file_none(self):
        """Tests that save_to_file method can be called from 
        Rectangle instance
        """
        Rectangle.save_to_file(None)
        filename = "Rectangle.json"
        data = ""
        with open(filename, "r") as f:
            for line in f:
                data += line

        self.assertEqual(data, "[]")

    def test_parent_save_to_file_empty_list(self):
        """Tests that save_to_file method when called with
        empty list as arg returns the expected value
        """
        Rectangle.save_to_file([])
        filename = "Rectangle.json"
        data = ""
        with open(filename, "r") as f:
            for line in f:
                data += line

        self.assertEqual(data, "[]")

    def test_parent_save_to_file_rectangle(self):
        """Tests that save_to_file method when called with
        list of Rectangles as arg returns the expected value
        """
        Rectangle.save_to_file([Rectangle(3, 3, 2, 2, 35)])
        filename = "Rectangle.json"
        data = ""
        with open(filename, "r") as f:
            for line in f:
                data += line

        self.assertEqual(
            data, '[{"x": 2, "y": 2, "id": 35, "height": 3, "width": 3}]')

    def test_rectangle_load_from_nonexistent_file(self):
        """Tests that load_from_file class method works
        as expected when file does not exist
        """
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_rectangle_load_from_existing_file(self):
        """Tests that load_from_file works when works
        as expected when called with None as argument
        """
        Rectangle.save_to_file(None)
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])


if __name__ == "__main__":
    unittest.main()
