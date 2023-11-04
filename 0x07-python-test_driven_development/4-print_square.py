#!/user/bin/python3
"""Defines a function that prints a square."""

def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Consist of the height/width of the square.
    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for t in range(size):
        [print("#", end="") for h in range(size)]
        print("")
