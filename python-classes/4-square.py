#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 3-square.py))
"""


class Square:
    """Initialize a class with init"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    "Defining the square"""
    def area(self):
        return self.__size * self.__size
