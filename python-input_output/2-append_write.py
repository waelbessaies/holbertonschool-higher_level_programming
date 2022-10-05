#!/usr/bin/python3
"""  a module that representes a function
that appends a string to a text file """


def write_file(filename="", text=""):
    """writes a string to a text file and return the number of characters
    args:
        filename: the name of the textfile
        text: the string to be inserted in the textfile
    return:
         number of char written into the textfile"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
