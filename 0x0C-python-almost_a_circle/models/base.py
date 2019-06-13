#!/usr/bin/python3
"""Base class module
"""
import json


class Base:
    """class base of other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        """
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
        if list_objs is None:
            list_ = []
        else:
            list_ = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation
        """
        if json_string is None or json_string is "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            inst = cls(1, 1)
        else:
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        l = []
        try:
            with open(filename, "r") as file:
                text = file.read()
        except:
            return l
        else:
            text_parsed = cls.from_json_string(text)
            for inst in text_parsed:
                obj = cls.create(**inst)
                l.append(obj)
            return l
