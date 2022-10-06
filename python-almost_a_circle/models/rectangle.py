#!/usr/bin/python3
"""
module
"""
from models.base import Base


class Rectangle(Base):
    """class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super() .__init__(id)

    @property
    def width(self):
        """methode"""
        return self.__width

    @property
    def height(self):
        """methode"""
        return self.__height

    @property
    def x(self):
        """methode"""
        return self.__x

    @property
    def y(self):
        """methode"""
        return self.__y
