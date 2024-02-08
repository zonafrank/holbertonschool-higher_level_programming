#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """initialization method for instances

        Args:
            first_name (str): first  name
            last_name (str): last name

            Return:
                Nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets dict of square.

            Args:
                attrs (list): list of attributes

            Returns:
                obj: dict with keys matching values in attrs
        """
        if not attrs:
            return self.__dict__
        result = {}
        for key in self.__dict__:
            if key in attrs:
                result[key] = self.__dict__[key]
        return result
