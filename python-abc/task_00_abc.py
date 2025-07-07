#!/usr/bin/env python3
"""
Module containing abstract Animal class and its subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an Animal
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that should return the animal's sound
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal
    """
    def sound(self):
        """
        Returns the sound of a dog
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal
    """
    def sound(self):
        """
        Returns the sound of a cat
        """
        return "Meow"
