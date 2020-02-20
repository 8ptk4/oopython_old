#!/usr/bin/python3
""" Queue - KMOM04 """

from node import Node
from errors import EmptyQueueException



class Queue:
    """ Queue Class """



    def __init__(self):
        """ Initialize class """

        self.head = None
        self.tail = None



    def is_empty(self):
        """ Check if queue is empty """

        return self.head is None



    def enqueue(self, value):
        """ Add node to queue according to FIFO """

        new_node = Node(value)

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

        if self.head is None:
            self.head = new_node



    def traverse(self):
        """ Traverse the nodes and list all Node values in Queue"""

        if self.head is None:
            raise EmptyQueueException("Empty queue.")

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next



    def dequeue(self):
        """ Remove the last node from queue  """

        value = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return value



    def peek(self):
        """ Peek the next """

        if self.head is None:
            raise EmptyQueueException("Empty queue.")

        return self.head.data



    def peek_current(self):
        """ Peek the current value """

        if self.tail is None:
            raise EmptyQueueException("Empty queue.")

        return self.tail.data



    def size(self):
        """ Size of the queue """

        current_node = self.head
        items = 0
        while current_node != None:
            items += 1
            current_node = current_node.next

        return items
