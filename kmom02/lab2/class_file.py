#!/usr/bin/python3
"""
    Person class and child classes
"""

class Person():
    """ Person Class """
    def __init__(self, name, ssn, address=""):
        self.name = name
        self._ssn = ssn
        self.address = address

    def get_name(self):
        """ Return name """
        return self.name

    def get_ssn(self):
        """ Return private ssn """
        return self._ssn

    def set_name(self, new_name):
        """ Rename """
        self.name = new_name

    def set_address(self, new_address):
        """ New address """
        self.address = new_address

    def to_string(self):
        """ Return string """
        return "Name: {name} SSN: {ssn} {address}".format(
            name=self.name,
            ssn=self._ssn,
            address=self.address
        )

class Address():
    """ Address Class """
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def to_string(self):
        """ Return string """
        return "Address: {city} {state} {country}".format(
            city=self.city,
            state=self.state,
            country=self.country
        )

class Teacher(Person):
    """ Child Class Teacher """
    def __init__(self, name, ssn, address):
        super(Teacher, self).__init__(name, ssn)
        self.courses = []

    def add_course(self, course):
        """ Appends course to list """
        self.courses.append(course)

    def remove_course(self, course):
        """ Remove course from list """
        self.courses.remove(course)

    def to_string(self):
        """ Return String """
        test = ", ".join(self.courses)

        return "Name: {name} SSN: {ssn} {address} Courses: {course}".format(
            name=self.name,
            ssn=self._ssn,
            address=self.address,
            course=test
        )

class Student(Person):
    """ Child Class Student """
    def __init__(self, name, ssn, address):
        super().__init__(name, ssn)
        self.courses_grades = []

    def add_course_grade(self, course, grade):
        """ Add grade to list """
        self.courses_grades.append((course, grade))

    def average_grade(self):
        """ Calculate average grade """
        nr_of_grades = 0
        grades = []
        for course in self.courses_grades:
            if course[1] != "-":
                nr_of_grades += 1
                grades.append(int(course[1]))

        grades_total = sum(grades)
        grades_average = grades_total / nr_of_grades

        return grades_average
