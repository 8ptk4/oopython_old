


class Node():
    """ class """

    def __init__(self, key, value, parent=None):
        """ init """

        self.key
        self.value
        self.left = None
        self.right = None
        self.parent = parent

    def has_left_child(self):
        return self.left is not None



    def has_right_child(self):
        return self.right is not None



    def __lt__(self, other):
        if isinstance(other, node):
            return self.key < other.key
        else:
            return self.key < other



    def __gt__(self, other):
        if isinstance(other, node):
            return self.key > other.key
        else:
            return self.key > other



    def __eq__(self, other):
        if isinstance(other, node):
            return self.key == other.key
        else:
            return self.key == other
