#!/usr/bin/python3
import json
"""module to load from json file
"""


def load_from_json_file(filename):
    """function that creates an Object from a JSON file
    """
    with open(filename) as file:
        return json.loads(file.read())
