#!/usr/bin/python3
"""Defines a base class."""

import json


class Base:
    """Represents the base."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if not json_string or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**obj) for obj in data]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in csv."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as file:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}\n")
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in csv."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                instances = []
                for line in file:
                    data = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(
                            id=int(data[0]),
                            width=int(data[1]),
                            height=int(data[2]),
                            x=int(data[3]),
                            y=int(data[4])
                        )
                    elif cls.__name__ == "Square":
                        instance = cls.create(
                            id=int(data[0]),
                            size=int(data[1]),
                            x=int(data[2]),
                            y=int(data[3])
                        )
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window that/and draws all the Rectangles and Squares."""
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")

        """Create a Turtle object."""
        pen = turtle.Turtle()

        """Draw Rectangles."""
        pen.speed(2)
        pen.color("blue")

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()

            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)

        """Draw Squares."""
        pen.color("red")  """Change the color for squares."""

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()

            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()
