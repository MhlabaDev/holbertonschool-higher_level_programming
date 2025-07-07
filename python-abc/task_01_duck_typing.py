#!/usr/bin/env python3
"""
Module for Shape abstract class and concrete implementations with duck typing
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a Shape
    """
    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter"""
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape
    """
    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate area of circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate circumference of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape
    """
    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing
    Args:
        shape: object with area() and perimeter() methods
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
