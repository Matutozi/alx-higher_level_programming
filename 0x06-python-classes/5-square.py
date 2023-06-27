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
        self.__size = size

    @property
    def size(self):
        """Retrieves the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets conditions for size attribute value"""
        if type(value) not in [int]:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square object"""
        return self.__size**2

    def my_print(self):
        """"Prints the square with character '#' """
        if self.__size == 0:
            print()
        else:
            length = self.__size
            while (length > 0):
                print('#' * self.__size)
                length -= 1
