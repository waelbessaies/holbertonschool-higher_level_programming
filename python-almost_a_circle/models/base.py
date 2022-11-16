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
        """returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """""JSON string to file"""""
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if not list_objs:
            pass
        else:
            for j in range(len(list_objs)):
                list_dict.append(list_objs[j].to_dictionary())
        lists = cls.to_json_string(list_dict)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances
        """
        filename = cls.__name__ + ".json"
        total = []
        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dictionary in obj_list:
                    total.append(cls.create(**dictionary))
                return total
        except:
            return total
