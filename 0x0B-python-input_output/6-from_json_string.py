#!/usr/bin/python3
import json
"""module to convert from json to obj
"""


def from_json_string(my_str):
    """function to return object represented by jason string
    """
    return json.loads(my_str)
