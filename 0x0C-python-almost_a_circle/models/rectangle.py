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
            raise ValueError("width must be > 0")
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

    def area(self):
        """Return the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Print in stdout the Rectangle instance with the character #."""
        for t in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the id of Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assign value argument to attributes according to their position."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for t, value in enumerate(args[:len(attrs)]):
                setattr(self, attrs[t], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
