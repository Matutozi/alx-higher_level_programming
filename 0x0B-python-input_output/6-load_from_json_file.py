#!/usr/bin/python3
"""6-load_from_json_file : load_from_json_file()"""


import json


def load_from_json_file(filename):
    """Loads python object from json file"""
    with open(filename, 'r', encoding="utf-8") as obj:
        return (json.load(obj))
