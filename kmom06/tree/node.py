#!/usr/bin/python3
""" Node - KMOM06 """

class Node():
    """ class """

    def __init__(self, key, value, parent=None):
        """ init """

        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent



    def has_left_child(self):
        """ has left child """

        return self.left is not None



    def has_right_child(self):
        """ has right child """

        return self.right is not None



    def has_both_children(self):
        """ has both childs """

        if self.has_left_child() and self.has_right_child():
            return True



    def has_parent(self):
        """ has parent """

        return self.parent is not None



    def is_left_child(self):
        """ is left child """

        if self.has_parent() and self.key < self.parent:
            return True



    def is_right_child(self):
        """ is right child """

        if self.has_parent() and self.key > self.parent:
            return True



    def __lt__(self, other):
        """ lt < """

        if isinstance(other, Node):
            return self.key < other.key
        return self.key < other



    def __gt__(self, other):
        """ gt > """

        if isinstance(other, Node):
            return self.key > other.key
        return self.key > other



    def __eq__(self, other):
        """ eq = """

        if isinstance(other, Node):
            return self.key == other.key
        return self.key == other
