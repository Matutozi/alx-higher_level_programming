#!/usr/bin/python3
"""
Module with class: Square
"""


class Square:
    """Square: defines a square """
    def __init__(self, size=0):
        """
        Instantiation with optional 'size'
        args: size (type 'int')
        raises type error if size is not an integer
        raises value error if size less than zero
        """
        if type(size) not in [int]:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square object"""
        return self.__size**2
