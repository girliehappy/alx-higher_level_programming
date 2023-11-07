#!/usr/bin/python3
"""Defines is_same_class function."""

def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    obj: The object to check.
    a_class: The class to check.
    Return: True if the object is exactly an instance of the specified class ; otherwise False.
    """
    return type(obj) is a_class
