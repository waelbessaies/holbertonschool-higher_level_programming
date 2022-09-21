#!/usr/bin/python3
'''
Task 5
'''


def text_indentation(text):
    '''
    Write a function that prints a text with 2 new lines after
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    newstr = 0
    for letter in text:
        if letter == " " and newstr == 0:
            continue
        newstr = 1
        if newstr == 1:
            if letter == "." or letter == "?" or letter == ":":
                print(f"{letter}\n")
                newstr = 0
            else:
                print(letter, end="")
