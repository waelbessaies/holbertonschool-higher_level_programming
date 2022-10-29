#!/usr/bin/python3
"""class"""
import json


class Base:
    """function init"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects


@staticmethod
def to_json_string(list_dictionaries):
    """update the class Base by adding the static methoddef to_json_string"""
    if list_dictionaries is None:
        return "[]"
    else:
        return json.dumps(list_dictionaries)
@staticmethod
def from_json_string(json_string):
    """method that write the list of the JSON from json string"""
    if json_string is None:
        return []
    else:
        return json.loads(json_string)
