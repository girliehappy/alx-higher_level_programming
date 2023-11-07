#!/usr/bin/python3
"""Defines a class Rectangle."""

class BaseGeometry:
    """Represents a BaseGeometry."""

    def area(self):
        """Public instance method 'area' that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Represents a Rectangle that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width(positive int): The width of the new rectangle.
            height(positive int): The height of the new rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns a value after width and height multiplication."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string."""
        return f"[Rectangle] {self.__width}/{self.__height}"
