#!/usr/bin/python3
"""
 class that create a Rectangle
"""


class Rectangle:
    """
    empty class Square that defines a Rectangle.
    """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializing Rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Class Method that calculates the Area of the rectangle
        Return:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Class Method that calculates the perimeter of the rectangle
        Return:
            The perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """__str__ method
        this method will print the rectangle on print() or str()
        """
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return my_str
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += '#'
            if i is not (self.__height - 1):
                my_str += "\n"
        return my_str

    def __repr__(self):
        """return a string representation of the rectangle
        """
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        ''' a method'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''This is a method'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
