#!/usr/bin/python3
"""square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init methode"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
