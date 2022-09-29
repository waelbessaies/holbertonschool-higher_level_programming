#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """this is a class"""

    def print_sorted(self):
        """Print a list in sorted """
        print(sorted(self))
