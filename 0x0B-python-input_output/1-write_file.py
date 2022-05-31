#!/usr/bin/python3
"""function
"""


def write_file(filename="", text=""):
    """
    function that  reads a text file  and prints it
    """
    with open(filename, "w", encoding="utf-8") as filename:
        filename.write(text)
    return len(text)
