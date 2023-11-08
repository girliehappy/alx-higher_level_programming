#!/usr/bin/python3
""""Defines a function that appends a string."""

def append_write(filename="", text=""):
    """
    Represents a function that append a string to the end of a text file (UTF8) and return the number of characters added.

    Args:
        filename(str): The name of the file to append to.
        text(str): The string to be appendded to the file.
    Returns:
        The number of characters that were added/appended.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
