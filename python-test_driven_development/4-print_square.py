#!/usr/bin/python3
"""
function  that prints a square with the character #
"""


def print_square(size):
    """prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print("")
