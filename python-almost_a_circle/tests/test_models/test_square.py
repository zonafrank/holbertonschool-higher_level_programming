#!/usr/bin/python3
"""Unittests for Square Class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_no_args(self):
        """Tests initialising Square with no args
        """
        self.assertRaises(TypeError, Square)

    def test_init_with_size(self):
        """Tests initialising Square with size
        """
        s = Square(3)
        self.assertEqual(s.size, 3)

    def test_init_with_size_and_x(self):
        """Tests initialising Square with size and x
        """
        s = Square(3, 5)
        self.assertEqual(s.x, 5)

    def test_init_with_size_x_and_y(self):
        """Tests initialising Square with size, x and y
        """
        s = Square(3, 5, 10)
        self.assertEqual(s.y, 10)

    def test_init_with_all_args(self):
        """Tests initialising Square with all args
        """
        s = Square(3, 5, 10, 25)
        self.assertEqual(s.id, 25)

    def test_init_with_size_string(self):
        """Tests initialising Square with string size
        """
        self.assertRaises(TypeError, Square, "10")

    def test_init_with_x_string(self):
        """Tests initialising Square with string x offset
        """
        self.assertRaises(TypeError, Square, 5, "10")

    def test_init_with_y_string(self):
        """Tests initialising Square with string y offset
        """
        self.assertRaises(TypeError, Square, 5, 10, "10")

    def test_init_with_negative_size(self):
        """Tests initialising Square with negative size
        """
        self.assertRaises(ValueError, Square, -1)

    def test_init_with_negative_x(self):
        """Tests initialising Square with negative x
        """
        self.assertRaises(ValueError, Square, 5, -1)

    def test_init_with_negative_y(self):
        """Tests initialising Square with negative y
        """
        self.assertRaises(ValueError, Square, 5, 1, -1)

    def test_init_with_zero_size(self):
        """Tests initialising Square with zero size
        """
        self.assertRaises(ValueError, Square, 0)

    def test_printable(self):
        """Tests that the instance can be stringified
        """
        s = Square(2, 0, 0, 25)
        self.assertEqual(s.__str__(), "[Square] (25) 0/0 - 2")

    def test_to_dictionary_method(self):
        """Tests that the dictionary representation is correct
        """
        s = Square(2, 0, 0, 30)
        d = s.to_dictionary()
        self.assertEqual(d, {'x': 0, 'y': 0, 'id': 30, 'size': 2})

    def test_update_method_no_args(self):
        """Tests the update method with no args
        """
        s = Square(2, 1, 1, 12)
        s.update()
        self.assertEqual(s.id, 12)

    def test_update_method_with_args(self):
        """Tests the update method with no args
        """
        s = Square(2, 1, 1, 12)
        s.update(25, 10, 3, 3)
        self.assertEqual(s.id, 25)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 3)

    def test_update_method_kwargs(self):
        """Tests that the update method works with kwargs
        """
        s = Square(2, 1, 1, 123)
        s.update(**{'id': 321, 'size': 5, 'x': 10, 'y': 10})
        self.assertEqual(s.id, 321)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

    def test_parent_create_method_kwargs(self):
        """Tests that the parent Base class' create method works with kwargs
        """
        s = Square.create(**{'id': 123, 'size': 5, 'x': 2, 'y': 2})
        self.assertEqual(s.id, 123)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)

    def test_parent_save_to_file_none(self):
        """Tests empty input with parent Base class' save_to_file method
        """
        Square.save_to_file(None)
        filename = "Square.json"

        data = ""
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data += line

        self.assertEqual(data, "[]")

    def test_parent_save_to_file_empty_list(self):
        """Tests empty list input with parent Base class' save_to_file method
        """
        Square.save_to_file([])
        filename = "Square.json"

        data = ""
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data += line

        self.assertEqual(data, "[]")

    def test_parent_save_to_file_list_square(self):
        """Tests list with Square instantiator as input with parent Base class' save_to_file method
        """
        Square.save_to_file([Square(3, 5, 5, 25)])
        filename = "Square.json"

        data = ""
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data += line

        self.assertEqual(
            data, "[{\"id\": 25, \"x\": 5, \"size\": 3, \"y\": 5}]")

    def test_parent_load_from_non_existant_file(self):
        """Tests loading from a non-existant file with parent Base class' load_from_file method
        """
        l = Square.load_from_file()
        self.assertEqual(l, [])

    def test_parent_load_from_non_existing_file(self):
        """Tests loading from an existing file with parent Base class' load_from_file method
        """
        Square.save_to_file(None)
        l = Square.load_from_file()
        self.assertEqual(str(l), "[]")


if __name__ == '__main__':
    unittest.main()
