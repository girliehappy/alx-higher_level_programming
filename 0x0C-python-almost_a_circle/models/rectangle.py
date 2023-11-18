#!/usr/bin/python3
""""Defines a class Rectangle that inherits from Base."""

from models.base import Base

class Rectangle(Base):
    """Represents a Rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the value of the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return the value of the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("Height must be a positive number")
        else:
            self.__height = value

    @property
    def x(self):
        """Return the value of x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Return the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
