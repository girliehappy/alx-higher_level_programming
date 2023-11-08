#!/usr/bin/python3
"""Defines a file-reading JSON function."""
import json

def load_from_json_file(filename):
    """
    Read and create an object from a JSON file.

    filename: The name of the JSON file to be read.
    Returns:
        The Python data structure represented by the JSON file.
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
