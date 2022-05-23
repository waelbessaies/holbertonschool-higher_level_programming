#!/usr/bin/python3
"""a python program that defines a rectangle"""


class Rectangle():
    """ empty class rectangle"""
    def __init__(self, width=0, height=0):
        """ the function arguments"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width property """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise(TypeError("width must be an integer"))
        if value < 0:
            raise(ValueError("width must be >= 0"))
        self.__width = value

    @property
    def height(self):
        """height property"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """height setter """
        if type(value) is not int:
            raise(TypeError("height must be an integer"))
        if value < 0:
            raise(ValueError("height must be >= 0"))
        self.__height = value

    def area(self):
        """ return the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """return the rectangle perimiter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """ print the rectangle area with the charchter '#' """
        return '\n'.join('#' * self.width for _ in range(self.height))