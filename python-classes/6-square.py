#!/usr/bin/python3
""" Program that creates a Square class"""


class Square:
    """ initializes the instance of the class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.

        Parameters:
        - size: Size of the square (default is 0)
        - position: Tuple representing the position of the square 
        (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Parameters:
        - value: New size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

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
        if ((not isinstance(value, tuple))
            or len(value) != 2
            or not all(isinstance(i, int) for i in value) 
            or any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' character based on size and position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
