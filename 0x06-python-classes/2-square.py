#!/usr/bin/python3
"""Square Module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes a New Square.
        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
