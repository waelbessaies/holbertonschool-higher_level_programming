#!/usr/bin/python3
""" Adds all arguments to a Python list"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    new_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    new_list = []

i = 1
if  len(argv) >0  != 1:
    while i < len(argv):
        new_list.append(argv[i])
        i += 1
save_to_json_file(new_list, "add_item.json")
