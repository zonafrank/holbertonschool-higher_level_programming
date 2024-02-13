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
