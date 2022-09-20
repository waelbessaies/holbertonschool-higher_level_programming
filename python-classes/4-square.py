#!/usr/bin/python3
"""
 class that create a Square
"""


class Square:
    """
     class Square that defines a square
    """

    def __init__(self, size=0):
        """ Initializing square , size: size of the side of the Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """calculates the area of the Square"""
        return self.__size * self.__size
