#!/usr/bin/python3
"""
module
"""
from models.base import Base


class Rectangle(Base):
    """class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
