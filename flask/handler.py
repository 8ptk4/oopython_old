#!/usr/bin/env python3
"""
Handler file
"""
from shape import Circle, Triangle, Square

shapes = []
message = []


def create_objects(form):
    """
        Create shapes.
    """
    message.clear()

    if form["shape_type"] == "Circle":
        circle = Circle(
            form["shape_type"],
            form["width"],
            form["height"],
            form["left"],
            form["top"],
            form["color"]
        )

        message.append(Circle.validate(circle))

        if Circle.validate(circle) == "Circle Added":
            shapes.append(circle)


    if form["shape_type"] == "Square":
        square = Square(
            form["shape_type"],
            form["width"],
            form["height"],
            form["left"],
            form["top"],
            form["color"]
        )

        message.append(Square.validate(square))

        if Square.validate(square) == "Square Added":
            shapes.append(square)


    if form["shape_type"] == "Triangle":
        triangle = Triangle(
            form["shape_type"],
            form["width"],
            form["height"],
            form["left"],
            form["top"],
            form["color"]
        )

        message.append(Triangle.validate(triangle))

        if Triangle.validate(triangle) == "Triangle Added":
            shapes.append(triangle)

def get_message():
    """
        Return messages provide by validation.
    """
    return message

def get_shapes():
    """
        Return shapes
    """
    return shapes
