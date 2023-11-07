#!/usr/bin/python3
"""Defines a function is_kind_of_class."""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or an instance of a class that inherited from, the specified class.

    obj: The object to check.
    a_class: The class to check against.
    Return: True if obj is an instance of a_class or its subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
