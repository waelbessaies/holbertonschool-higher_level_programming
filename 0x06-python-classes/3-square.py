#!/usr/bin/python3
""" Defining a Square """


class Square:
    """Square class
    Attributes: size (int): size of the squre """

    def __init__(self, size=0):
        """size initialization"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
