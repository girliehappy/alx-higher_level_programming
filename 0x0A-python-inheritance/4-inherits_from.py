#!/usr/bin/python3
"""Defines a function inherits_from."""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    obj: The object to check.
    a_class: The class to check against.
    Return: True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class)
