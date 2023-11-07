#!/usr/bin/python3
"""Defines a class Square."""

class BaseGeometry:
    """Represents a BaseGeometry."""

    def area(self):
        """The public instance 'area' that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """The public instance that validates an integer value."""
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
            width(positive int): The new width of Rectangle.
            height(positive int): The new height of Rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a strin that specifies Rectangle and its width and height values."""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """Represents a class Square that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initializes a new Square.

        Size must be private. No getter or setter.
        Size must be a positive integer, validated by integer_validator.
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of width and height by mutiplication."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return a Square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
