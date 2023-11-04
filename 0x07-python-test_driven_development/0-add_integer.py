#!/user/bin/python3
"""Defines a function that adds two integers."""

def add_integer(a, b=98):
    """Returns an integer after adding a and b.

    Floats are first casted to integers before addition is performed.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(b, float))):
        raise TypeError("a must be an integer.")
    if ((not isinstance(a, float) and not isinstance(b,int))):
        raise TypeError("b must be an integer.")
    return (int(a) + int(b))
