#!/usr/bin/python3
"""Defines a class BaseGeometry."""

class BaseGeometry:
    """Represents a BaseGeometry."""

    def area(self):
        """The specified public instance method 'area' that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates int value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
