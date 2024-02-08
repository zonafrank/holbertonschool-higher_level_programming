#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate argument to be integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
