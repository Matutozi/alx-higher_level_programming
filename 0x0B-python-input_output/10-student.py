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
