#!/usr/bin/python3
"""Defines a functon that writes a strin to a text file."""

def write_file(filename="", text=""):
    """
    Represents function that writes a string to a text file (UTF8) and return the number of characters written.

    filename: The name of the file to write to.
    text: The string to be written to the file.
    return: The number of characters that are written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count
