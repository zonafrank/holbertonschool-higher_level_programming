#!/usr/bin/python3
"""module for Base class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method"""
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
