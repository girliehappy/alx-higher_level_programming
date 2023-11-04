#!/usr/bin/python3
"""Defines a function that adds two integers."""

def add_integer(a, b=98):
    """Returns an integer after adding a and b.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add (the default is 98).

    Returns:
        int: The result of adding the values, a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if (not isinstance(a, int) and not isinstance(b, float)):
        raise TypeError("a must be an integer.")
    if (not isinstance(a, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer.")
    a = int(a) if isinstance(a, float) else int(a)
    b = int(b) if isinstance(b, float) else int(b)
    return a + b
