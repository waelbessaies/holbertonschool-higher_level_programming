#!/usr/bin/python3
"""Square module
This module defines a Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    this is the class for square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method
        this method will print the rectangle on print() or str()
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """to_dictionary Method
        this method will return the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
