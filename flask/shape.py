#!/usr/bin/env python3
"""
    Parent / Child classes for drawing shapes.
    Methods for validation and calculating area.
"""
import math


class Shape():
    """
        Class for Shape
    """
    #pylint: disable-msg=too-many-arguments
    def __init__(self, shape, width, height, left, top, color):
        self.shape = shape
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.color = color


    def get_shape_type(self):
        """
        Returns the type
        """
        return self.shape


    def get_width(self):
        """
        Returns the type
        """
        return self.width


    def get_height(self):
        """
        Returns the type
        """
        return self.height


    def get_left(self):
        """
        Returns the type
        """
        return self.left


    def get_top(self):
        """
        Returns the type
        """
        return self.top


    def get_color(self):
        """
        Returns the type
        """
        return self.color


    def get_area(self):
        """
            Force subclasses to override this method.
        """
        raise NotImplementedError("This method needs to be implemented in \
child classes!")


    def validate(self):
        """
            Force subclasses to override this method.
        """
        raise NotImplementedError("This method needs to be implemented in \
child classes!")


class Circle(Shape):
    """
        Child class Circle
    """
    def draw_shape(self):
        """
            Return inline css
        """
        return "width: {width}px; height: {height}px; border-radius: 50%; \
background-color: {color}; top: {top}px; left: {left}px;".format(
    width=self.width,
    height=self.height,
    color=self.color,
    top=self.top,
    left=self.left
)


    def validate(self):
        """
            Validate that circle width and height is the same.
        """
        if self.width == "" or self.height == "":
            return "Width and Height needs to have a value."
        elif self.width == self.height:
            return self.shape + " Added"
        elif self.width < self.height:
            return "Height needs to be same as width."
        elif self.width > self.height:
            return "Width need to be same as height."


    def get_area(self):
        """
            Get the area of circle rounded to one decimal.
        """
        return round(
            math.pi * (float(self.width) / 2) * (float(self.width) / 2), 1)


class Square(Shape):
    """
        Child class Square
    """
    def draw_shape(self):
        """
            Inline css that will be used to draw the shape.
        """
        return "width: {width}px; height: {height}px; \
background-color: {color}; top: {top}px; \
left: {left}px;".format(
    width=self.width,
    height=self.height,
    color=self.color,
    top=self.top,
    left=self.left
)


    def validate(self):
        """
            Validate that circle width and height is the same.
        """
        if self.width == "" or self.height == "":
            return "Width and Height needs to have a value."
        elif self.width == self.height:
            return self.shape + " Added"
        elif self.width < self.height:
            return "Height needs to be same as width."
        elif self.width > self.height:
            return "Width need to be same as height."


    def get_area(self):
        """
            Return Area of Square
        """
        return float(self.width) * float(self.height)


class Triangle(Shape):
    """
        Child class Square
    """

    def draw_shape(self):
        """
            Inline css that will be used to draw the shape.
        """
        return "width: 0; height: 0; border-bottom: {height}px solid {color}; \
border-right: {width}px solid transparent; top: {top}px; \
left: {left}px;".format(
    width=self.width,
    height=self.height,
    color=self.color,
    top=self.top,
    left=self.left,
)


    def validate(self):
        if self.width != "" and self.height != "":
            return self.shape + " Added"
        elif self.width == "" and self.height == "":
            return "Height and width needs to have values"
        elif self.height != "" and self.width == "":
            return "Width needs to have a value"
        elif self.height == "" and self.width != "":
            return "Height needs to have a value"


    def get_area(self):
        """
            Return Area of Triangle
            (Base * Height) / 2
        """
        return (float(self.width) * float(self.height)) / 2
