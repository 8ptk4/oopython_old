#!/usr/bin/env python3

"""
f09190624dbd5b9b032e5d4f0c019818
oopython
lab3
v2
paka17
2020-02-01 21:07:35
v4.0.0 (2019-03-05)

Generated 2020-02-01 22:07:36 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `18` up to `35`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_sum(head, tail):
    if head <= tail:
        return head + recursive_sum((head + 1), tail)
    else: 
        return 0

ANSWER = recursive_sum(18, 35)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
# If its an empty list return `0`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

sum = [4, 5, 6, 11, 9, 1, 2, 3, 8]

def recursive_sum(sum):
    
    if len(sum) == 0:
        return 0
    else:
        return sum[0] + recursive_sum(sum[1:])

ANSWER = recursive_sum(sum)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `2` in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

numbers = [4, 5, 6, 11, 9, 1, 2, 3, 8]

def recursive_search(numbers, index, value):
    if not numbers:
        return -1
    elif numbers[0] == value:
        return index
    return numbers[0] == value or recursive_search(numbers[1:], (index + 1), value)

ANSWER = recursive_search(numbers, 0, 2)

# I will now test your answer - change false to true to get a hint).
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `19` in
# the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

numbers = [4, 5, 6, 11, 9, 1, 2, 3, 8]

ANSWER = recursive_search(numbers, 0, 19)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `5` to the
# power of `6`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_power(num, exp):
    if (exp == 1):
        return num
    if (exp != 1):
        return (num * recursive_power(num, exp - 1))

ANSWER = recursive_power(5, 6)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "Backwards" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursion_reverse(string):
    if string is "":
        return string
    else: 
        return string[-1] + recursion_reverse(string[:-1])

ANSWER = recursion_reverse("Backwards")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)


dbwebb.exit_with_summary()
