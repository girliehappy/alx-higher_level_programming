#!/usr/bin/python3
"""Square Module."""

class Square:
    """Defines a square."""

    def __init__(self, size):
        """Initializes a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """In order to Print the square with the # character."""
        for h in range(0, self.__size):
            [print("#", end="") for a in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
