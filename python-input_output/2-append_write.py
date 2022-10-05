#!/usr/bin/python3
"""
a module that representes a function
that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    a function that appends a string to the end of a text file
    and returns the number of characters
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)