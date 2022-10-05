#!/usr/bin/python3
""" a function that open  a file and write a text in it """


def write_file(filename="", text=""):
    """writes a string to a text file and return the number of characters"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
