#!/usr/bin/python3
"""module name: rectangle, Class: Rectangle
"""


from models.base import Base


import json


class Rectangle(Base):
    """Defines a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the instance atributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ to create private instance attributes for each
        parameter"""
    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x atttribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Shows a visual representation of the rectangle"""
        for d in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(self.__x * ' ', self.__width * '#'))

    def display(self):
        """prints the rectangle instance using "#" character"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/self.__y} - {self.__width}/{self.__height}")
