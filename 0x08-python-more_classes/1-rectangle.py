#!/usr/bin/python3
"""Defines a Class Rectangle."""


class Rectangle:
    """Represents a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve/Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:   
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve/Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
