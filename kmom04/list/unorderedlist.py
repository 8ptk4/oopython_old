#!/usr/bin/python3
""" Unordered list - KMOM04 """

from node import Node
from errors import IndexErrorException
from errors import ValueErrorException
from errors import AttributeErrorException

class UnorderedList:
    """ Unordered list class"""



    def __init__(self):
        """ Initialize list head """
        self.head = None



    def is_empty(self):
        """ Return True/False if list is empty or not """
        
        return self.head == None



    def add(self, data):
        """ Add new node last in the list """

        current_node = self.head
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

            return None
        
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node



    def insert(self, index, data):
        """ Add new node at a specific index, raise exception if index doesnt excist """

        current_node = self.head
        new_node = Node(data)
        previous_node = None
        i = 0

        if index > self.size() or index < 0:
            raise IndexErrorException("Error: Index doesnt exist")

        while i < index:

            previous_node = current_node
            current_node = current_node.next

            i += 1

        if index == 0:
            self.head = new_node
            new_node.next = current_node
        elif i == index:
            previous_node.next = new_node
            new_node.next = current_node



    def set(self, index, data):
        """ Replace value at a specific index, raise exception if index doesnt excist """

        current_node = self.head

        i = 0
    
        if index > (self.size() - 1) or index < 0:
            raise IndexErrorException("Error: Index doesnt exist")

        while current_node is not None:
            if i == index:
                current_node.data = data
        
            i += 1
            current_node = current_node.next



    def size(self): # Integer
        """ Return amount of elements in the list """
    
        current_node = self.head
        
        i = 0
        while current_node is not None:
            i += 1
            current_node = current_node.next

        return int(i)



    def get(self, index): # data
        """ Return value at a specific index else raise an exception """

        current_node = self.head

        i = 0
        while current_node is not None:
            if i == index:
                return current_node.data
        
            i += 1
            current_node = current_node.next

        raise IndexErrorException("IndexError: Out of index")



    def index_of(self, data):
        """ Return the index of a specific value, if values doesnt excist raise exception """
        
        current_node = self.head

        i = 0
        while current_node is not None:
            if current_node.data == data:
                return int(i)

            i += 1
            current_node = current_node.next

        raise ValueErrorException("ValueError: No index with that value")



    def print_list(self):
        """ Output all the values in the list """

        current_node = self.head
        i = 0
        while current_node is not None:
            i += 1
            print("{}: {}".format((i - 1), current_node.data), end=" ")
            current_node = current_node.next



    def remove(self, data):
        """ Remove node matching a specific value, if values doesnt excist raise exception """

        current_node = self.head
        previous_node = None

        while current_node is not None:
            if data == current_node.data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return

            previous_node = current_node
            current_node = current_node.next

        raise ValueErrorException("ValueError: Value doesnt excist")
