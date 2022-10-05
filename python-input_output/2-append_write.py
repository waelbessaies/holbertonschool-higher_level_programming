#!/usr/bin/python3
"""  a module that representes a function
that appends a string to a text file """


def write_file(filename="", text=""):
    """
    A function that appends a string to the end of a text file
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
