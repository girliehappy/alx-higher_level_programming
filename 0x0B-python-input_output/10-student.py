#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (string): The first name of the student.
            last_name (string): The last name of the student.
            age (integer): The age of the student.
        """
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrives a dictionary representation of the Student.

        If attrs is a list of string, only attribute names contained in this list must be retrieved.

        Args:
            attrs (list): The attributes to represent.
        """
        
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {h: getattr(self, h) for h in attrs if hasattr(self, h)}
        return self.__dict__
