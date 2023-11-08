#!/usr/bin/python3
"""Defines a file-writing JSON function."""
import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj: The object to be written into the file.
        filename: The name of the file to save the JSON representation.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
