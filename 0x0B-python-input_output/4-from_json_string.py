#!/usr/bin/python3
"""Defines an object-to-JSON function."""
import json

def from_json_string(my_str):
    """
    Return the Python object (data structures) represented by a JSON string.

    my_str: The JSON string that's to be converted to a Python object.
    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

