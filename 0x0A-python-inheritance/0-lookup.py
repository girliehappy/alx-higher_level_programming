#!/usr/bin/python3
"""Defines a function lookup."""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    obj: The object to check.
    Return: A list object.
    """
    return dir(obj)
