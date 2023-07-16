#!/usr/bin/python3
"""module name: rectangle, Class: Rectangle
"""


from models.base import base


import json


class Rectangle(Base):
    """Defines a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the instance atributes"""
        assert type(height) == int and type(x) == int and
        type(y) == int
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ to create private instance attributes for each
        parameter"""
    @property
    def width(self):
        return self.__width

    @width.setter(self, value):
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter(self, value):
        self.__y = value
