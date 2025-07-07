#!/usr/bin/python3
"""
This module contains a function named
class_to_json
"""


def class_to_json(obj):
    """
    function that returns the dictionary
    description with simple data structure
    for JSON serialization of
    an object (list, dictionary, string, integer
    and boolean)
    """
    return obj.__dict__
