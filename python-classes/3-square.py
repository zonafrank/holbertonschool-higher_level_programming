#!/usr/bin/python3
""" Program that creates a Square class"""


class Square:
    """ initializes the instance of the class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the area of the square"""
        return self.__size * self.__size
