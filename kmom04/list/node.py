#!/usr/bin/python3
""" Unordered list - KMOM04 """

class Node:
    """ Node class """



    def __init__(self, data, next=None):
        """
        Initialize object with the data and set next to None.
        next will be assigned later when new data needs to be added.
        """
        self.data = data
        self.next = next
