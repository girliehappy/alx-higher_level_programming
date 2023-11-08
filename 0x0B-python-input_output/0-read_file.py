#!/usr/bin/python3
""""Defines a function that reads a text file."""

def read_file(filename=""):
    """
    Reads and prints the contents of a text file (UTF8) to stdout.

    filename: The name of the file to read.
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
