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
        self.__width = val

    @property
    def height(self):
        """getter method to return self.__height"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter method for self.__height"""
        self.__height = val

    @property
    def x(self):
        """getter method to return self.__x"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter method for self.__x"""
        self.__x = val

    @property
    def y(self):
        """getter method to return self.__y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter method for self.__y"""
        self.__y = val
