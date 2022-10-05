#!/usr/bin/python3
'''Task 2'''


def write_file(filename="", text=""):
    '''append a string at eof'''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
