#!/user/bin/python3
"""Defines a function that prints a name."""

def say_my_name(first_name, last_name=""):
    """Prints a name, both first and last.
    
    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed.
    Raises:
        TypeError: if either of the names is not a string.
    """
    if not isinstance(first_name str):
        raise TypeError("First_name must be a string")
    if not isinstance(last_name str):
        raise TypeError("Last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
