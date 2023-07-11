#!/usr/bin/python3
"""5-save_to_json_file : save_to_json_file()"""


import json


def save_to_json_file(my_obj, filename):
    """Serializes a python object"""
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
