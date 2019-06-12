#!/usr/bin/python3
"""Base class module
"""
import json


class Base:
    """class base of other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON representation of object
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON to file
        """
        filename = "{}.json".format(list_objs[0].__class__.__name__)
        with open(filename, "w+") as file:
            else:
                for i in list_objs:
                    file.write(cls.to_json_string(i), default="[]")
