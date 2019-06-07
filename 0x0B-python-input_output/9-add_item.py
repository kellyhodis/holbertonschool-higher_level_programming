#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
"""module to load, add, and save
"""


py_list = []
if len(sys.argv) > 1:
    for i in range (1, len(sys.argv)):
        py_list.append(sys.argv[i])
save_to_json_file(py_list, "add_item.json")
