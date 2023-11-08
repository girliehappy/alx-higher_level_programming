#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a string object.

    my_obj: The object to be converted to JSON.
    Returns:
        The JSON representation of a string object.
    """
    return json.dumps(my_obj)
