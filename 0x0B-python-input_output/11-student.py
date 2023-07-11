#!/usr/bin/python3
"""Module : 10-student, Class : Student"""


class Student:
    """Defines a student
        Attributes: first_name, last_name, age
        Method: __init__(), to_json()
    """
    def __init__(self, first_name, last_name, age):
        """initialise attributes for every class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of a Student instance
            Args: attrs (list of attributes to retrieve in dictionary)"""
        if attrs is not None:
            my_d = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return my_d
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of a student instance
            Args: json (a dictionary)
                The dictionary key becomes the instance attribute
                The dictionary key value becomes the value of the attribute"""
        for k, v in json.items():
            self.__setattr__(k, v)
