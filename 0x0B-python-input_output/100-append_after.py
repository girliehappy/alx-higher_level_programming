#!/usr/bin/python3
"""Defines a function that inserts text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a specific string in a file.

    Args:
        filename (str): The name in which the file bears.
        search_string (str): The string to be searched for within the file.
        new_string (str): The string to be inserted.
    """
    
    text = ""
    with open(filename) as h:
        for line in h:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
