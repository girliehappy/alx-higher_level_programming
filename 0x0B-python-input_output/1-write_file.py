#!/usr/bin/python3
"""Defines a functon that writes a strin to a text file."""


def write_file(filename="", text=""):
    """
    Represents function that writes a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename: The name of the file to write to.
        text: The string to be written to the file.
    Returns:
        The number of characters that are written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
