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
        '''This is a method'''
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__:
                dic[i] = self.__dict__[i]
        return dic
    def reload_from_json(self, json):
        '''This is a method'''
        for i, j in json.items():
            setattr(self, i, j)