#!/usr/bin/python3
"""task 1"""


class MyList(list):
    def print_sorted(self):
        '''Write a class MyList that inherits from list:'''
        print(sorted(self))
