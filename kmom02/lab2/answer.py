#!/usr/bin/env python3

"""
1c84c38585a2695f690f5a29fa96b81a
oopython
lab2
v2
paka17
2018-01-23 16:24:31
v2.3.9 (2017-12-28)

Generated 2018-01-23 17:24:31 by dbwebb lab-utility v2.3.9 (2017-12-28).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb
from class_file import Person, Address, Teacher, Student

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* method for both "name" and "ssn". Only Create a *set* method
# for "name".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Zimba` and ssn `228474-2825`.
#
#
# Answer with per\'s get method for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#

per = Person("Zimba", "228474-2825")

ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create a method, in Address, called **to_string**, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Add the instance attribute **address** to class Person. It's value should
# be sent as argument to constructor, give it a default value of and empty
# string, `""`.
# Create a set method for attribute "address".
# Create a method, in Person, called **to_string**, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"`. Use Address'
# to_string method to get address data.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Katar`, the state `Blekinge` and the country `Illian`.
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

# New instance of the class Address with city, state, country
address1 = Address("Katar", "Blekinge", "Illian")

# Use set method in Person to add the address object above to per object.
per.set_address(address1.to_string())

ANSWER = per.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person". In
# the constructor add the instance attribute "courses" and initiate it to and
# empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Create the method **remove_course**, it should take one argument and remove
# if from the course list attribute.
# Overload the **to_string** method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Tip, use `super(Teacher, self)` to access base
# method.
#
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Katar`, the state `Skane` and the country `Illian`.
# Create a new instance of the class Teacher. Initiate it with the name `Ove`
# and ssn `930807-7536` and the aforementioned Address object.
# Use the add_course method to add the following courses, `htmlphp`,
# `ramverk1` and `design`.
#
#
# Answer with the Teacher object's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

address2 = Address("Katar", "Skane", "Illian")

teacher1 = Teacher("Ove", "930807-7536", address2)
teacher1.set_address(address2.to_string())

teacher1.add_course("htmlphp")
teacher1.add_course("ramverk1")
teacher1.add_course("design")

ANSWER = teacher1.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person". In
# the constructor add the instance attribute "courses_grades" and initiate it
# to and empty list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Amador`, the state `The Aiel Waste` and the country
# `Commonwealth`.
# Create a new instance of the class Student. Initiate it with the name
# `Buster` and ssn `619172-0731` and the aforementioned Address object.
# Use the add_course_grade method to add the following courses, `ramverk2`
# with grade `2`, `design` with grade `-` and `ramverk2` with grade `5`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

address3 = Address("Amador", "The Aiel Waste", "Commonwealth")

student1 = Student("Buster", "619172-0731", address3)
student1.set_address(address3.to_string())

student1.add_course_grade("ramverk2", "2")
student1.add_course_grade("design", "-")
student1.add_course_grade("ramverk2", "5")

ANSWER = student1.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)


dbwebb.exit_with_summary()
