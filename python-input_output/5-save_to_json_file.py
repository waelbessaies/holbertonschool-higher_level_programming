#!/usr/bin/python3
'''This is a moudle'''
import json


def save_to_json_file(my_obj, filename):
    '''This is a function'''
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
