#!/usr/bin/python3
""" function

"""


def read_file(filename=""):
    """
    function that  reads a text file  and prints it
    """
    with open(filename, "r", encoding="utf-8") as filename:
        print(filename.read(), end="")
