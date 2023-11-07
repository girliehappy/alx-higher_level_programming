#!/usr/bin/python3
"""Dwfines a add_attribte function."""

def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.

    obj: The object to add the attribute to.
    attr_name: The name of the attribute.
    attr_value: The value of the attribute.
    TypeError: If the object can't have new attributes.
    """

    if hasattr(obj, attr_name):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
