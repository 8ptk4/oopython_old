#!/usr/bin/env python3
"""
    Classes for lab1
"""
#class
class Cat():
    """ Cat class """
    #static variable
    nr_of_paws = 4

    #constructor
    def __init__(self, eye_color, name, lives_left=-1):
        self.eye_color = eye_color
        self.name = name
        self.lives_left = lives_left

    #methods "functions inside class"
    def get_eye_color(self):
        """
            Get method that returns eye color
        """
        return self.eye_color

    def get_name(self):
        """
            Get method that returns name
        """
        return self.name

    def get_lives_left(self):
        """
            Get method that returns lives left
        """
        return self.lives_left

    def get_nr_of_paws(self):
        """
            Get method that returns nr of paws
        """
        return self.nr_of_paws

    def set_lives_left(self, new_lives):
        """
            Set method that updates lives left
        """
        self.lives_left = new_lives

    def description(self):
        """
            Method that returns string
        """
        return "My cats name is {}, has {} eyes and {} \
lives left to live.".format(
    self.name,
    self.eye_color,
    self.lives_left
)


#class
class Dog():
    """
        Dog class
    """
    #static variable
    nr_of_paws = 4

    #constructor
    def __init__(self, eye_color, name, lives_left=1):
        self.eye_color = eye_color
        self.name = name
        self.lives_left = lives_left

    #methods "functions inside class"
    def get_eye_color(self):
        """
            Get method that returns eye color
        """
        return self.eye_color

    def get_name(self):
        """
            Get method that returns name
        """
        return self.name

    def get_lives_left(self):
        """
            Get method that returns lives left
        """
        return self.lives_left

    def get_nr_of_paws(self):
        """
            Get method that returns nr of paws
        """
        return self.nr_of_paws

    def set_lives_left(self, new_lives):
        """
            Set method that updates lives left
        """
        self.lives_left = new_lives

    def description(self):
        """
            Method that returns a string
        """
        return "My dogs name is {}, has {} \
eyes and {} lives left to live.".format(
    self.name,
    self.eye_color,
    self.lives_left
)


class Time():
    """
        Time class
    """
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def info(self):
        """
            Method that adds a 0 infront of number if the number is
            less then 10.
        """
        time = [self.hours, self.minutes, self.seconds]
        time_formated = ""

        for i in time:
            if i < 10:
                i = str(i).zfill(2)
            time_formated += str(i) + "-"

        return time_formated[:-1]

    @staticmethod
    def time_seconds(time):
        """
            Static method that converts time to seconds.
        """
        test = time.split("-")
        hours = test[0]
        minutes = test[1]
        seconds = test[2]

        tot = ((int(hours) * 3600) + (int(minutes) * 60) + int(seconds))
        return tot

    def __add__(self, other):
        return self.time_seconds(self.info()) + other.time_seconds(
            other.info()
        )

    def __iadd__(self, other):
        self.hours += other.hours
        self.seconds += other.seconds
        self.minutes += other.minutes

        return self

    def __lt__(self, other):
        if self.time_seconds(self.info()) < other.time_seconds(other.info()):
            return bool(True)
        return bool(False)
