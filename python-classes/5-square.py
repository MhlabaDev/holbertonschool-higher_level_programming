#!/usr/bin/python3
"""
Add print method in class Square.
"""


class Square:
    """
    Class that defines a square.
    Attributes:
        size(int): size of the square - private attribute.
    """

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        if self.__size == 0:
            print()

        i = 1
        while i <= self.__size:
            j = 1
            while j <= self.__size:
                print("#", end='')
                j += 1
            print()
            i += 1

    @property
    def size(self):
        """Property that retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter that sets the value of size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
