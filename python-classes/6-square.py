#!/usr/bin/python3
""" Program that creates a Square class"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """ initializes the instance of the class"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """
        that prints in stdout the square with the character #
        prints a new line of size is zero
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """getter method for position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position property"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int)) or (not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
