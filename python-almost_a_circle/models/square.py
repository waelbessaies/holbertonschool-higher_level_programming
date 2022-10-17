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

    def update(self, *args, **kwargs):
        '''This is a method'''
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """a method to return the dictionary """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
