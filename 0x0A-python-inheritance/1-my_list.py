#!/usr/bin/python3
"""Defines a class MyList."""

class Mylist(list):
    """Represents a class MyList."""

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        All the elements of the list will be of type int.
        """
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=' ')
        print()
