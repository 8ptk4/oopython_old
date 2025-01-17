#!/usr/bin/env python3
"""
Class file for Employee
"""
import random

class Employee():
    """
    Class for Employee
    """

    def __init__(self, firstname, lastname, salary):
        """
        init method
        """
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.id = random.sample(range(10), 4)

    def get_salary(self):
        """
        Returns the salary
        """
        return self.salary

    def get_id(self):
        """
        Returns the employement id
        """
        return "".join(map(str, self.id))

    def get_name(self):
        """
        Returns name
        """
        return self.firstname + " " + self.lastname
