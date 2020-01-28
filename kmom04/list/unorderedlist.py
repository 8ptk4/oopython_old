#!/usr/bin/python3

from node import Node

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

            return True
        
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node

    def insert(self, index, data):
        """ Add new node at a specific index, raise exception if index doesnt excist """
        pass

    def set(self, index, data):
        """ Replace value at a specific index, raise exception if index doesnt excist """
        

    def size(self): # Integer
        """ Return amount of elements in the list """
        
        current_node = self.head
        i = 0
        while current_node is not None:
            i += 1
            current_node = current_node.next

        return i

    def get(self, index): # data
        """ Return value at a specific index """
        pass

    def index_of(self, data): # Integer
        """ Return the index of a specific value, if values doesnt excist raise exception """
        pass

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
        
        # Exception here..
