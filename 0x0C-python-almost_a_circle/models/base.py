#!/usr/bin/python3
"""Module name: base, Class: Base
"""


import json


class Base:
    """This is the base of all the other classes
        method: __init__()"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
