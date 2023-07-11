#!/usr/bin/python3
"""Module : 9-student, Class : Student"""


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

    def to_json(self):
        """Retrieves dictionary representation of a Student instance"""
        return (self.__dict__)
