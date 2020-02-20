#!/usr/bin/python3
""" Queue - KMOM04 """



class Node:
    """ Node class """



    def __init__(self, data, next_node=None):
        """
        Initialize object with the data and set next to None.
        next will be assigned later when new data needs to be added.'
        """

        self.data = data
        self.next = next_node
