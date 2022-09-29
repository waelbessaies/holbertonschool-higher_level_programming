#!/usr/bin/python3
'''Task 6'''


class BaseGeometry:
    '''This is is a class'''

    def area(self):
        ''' a function'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' a function'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
