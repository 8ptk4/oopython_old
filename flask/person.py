#!/usr/bin/env python3
"""
Person Class
"""
from datetime import date

class Person():
    """ Represents information about person """

    def __init__(self, first, last, born, course, img):
        self.first = first
        self.last = last
        self.born = born
        self.course = course
        self.img = img

    def name(self):
        """
        Returns the first and last name concatinated togeather for ease of use
        """
        return self.first + " " + self.last

    def age(self):
        """
        Returns person age from yyyymmdd by calculation against datetime
        object that way we dont have to edit this ever again nor set the
        age every year
        """
        today = date.today()
        born_date = self.born.split("-")
        born_year = born_date[0]
        born_month = born_date[1]
        born_day = born_date[2]
        return today.year - int(born_year) - (
            (today.month, today.day) < (int(born_month), int(born_day))
            )

    def image(self):
        """ Create path to image provided by the object """
        path = "static/images/" + self.img
        return path
