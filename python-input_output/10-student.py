#!/usr/bin/python3
'''task 9'''


class Student:
    '''a class'''

    def __init__(self, first_name, last_name, age):
        '''Public instance attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''public  method'''
        if attrs is None:
            return self.__dict__