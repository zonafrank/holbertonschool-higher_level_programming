#!/usr/bin/python3
""" Program that creates a Square class"""


class Square:
    """ Defines a Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.

        Parameters:
        - size: Size of the square (default is 0)
        - position: Tuple representing the position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter method for setting the size of the square.

        Parameters:
        - value: New size value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """
        Prints the square using '#' character based on size and position.
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
        """
        Getter method for retrieving the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Parameters:
        - value: New position value (tuple of 2 positive integers)
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int)) or (not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
