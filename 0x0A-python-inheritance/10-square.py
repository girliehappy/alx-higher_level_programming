#!/usr/bin/python3
"""Defines a class square."""

class BaseGeometry:
    """Represents a BaseGeometry."""

    def area(self):
        """Public instance that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates inteer values."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Represents a class Rectangle that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        Args:
            width(positive int): The width of the new Rectangle.
            height:(positive int): The height of the new Rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns a value when width and height is multiplied."""
        return self.__width * self.__height

    def __str__(self):
        """Prints a string that specifies rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """Repreaents a class Square that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initializes a new Square.

        Size must be private. No getter or setter.
        Size must be a positive integer, validated by integer_validator.
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Prints a string that specifies square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
