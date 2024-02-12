#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class which inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method for Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method to return self.__width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter method for self.__width"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter method to return self.__height"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter method for self.__height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter method to return self.__x"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter method for self.__x"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter method to return self.__y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter method for self.__y"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val
