#!/usr/bin/python3
""" Program that creates a Square class"""


class Square:
    """ initializes the instance of the class"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """ Returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """ getter method for size property"""
        return self.__size

    @size.setter
    def size(self, size):
        """ setter method for size property """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
