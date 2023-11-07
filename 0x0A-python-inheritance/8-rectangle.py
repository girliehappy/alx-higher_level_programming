#!/usr/bin/python3
"""Defines a class Rectangle."""

class BaseGeometry:
    """Represents a BaseGeometry."""
    
    def area(self):
        """The specified public instance method area that raises an exception."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.

        Name is always a string.
        If value is not an integer: raise a TypeError exception, with the message <name> must be an integer.
        If value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Represents a class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width(positive int): The width of the new rectangle.
            height(positive int): The height of the new rectanle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
