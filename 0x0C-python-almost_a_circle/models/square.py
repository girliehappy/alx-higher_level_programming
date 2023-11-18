#!/usr/bin/python3
"""Defines the class Square."""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a Square that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of width."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of width."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return width or height."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assign attributes according to their position."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args[:len(attrs)]):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
