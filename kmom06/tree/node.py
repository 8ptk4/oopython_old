


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
        """ returnera True om noden har en left child nod, annars False. """

        return self.left is not None



    def has_right_child(self):
        """ returnera True om noden har en right child nod, annars False. """

        return self.right is not None



    def has_both_children(self):
        """
        returnera True om noden har en left och en right child nod, annars False.
        """

        return self.right and self.left is not None



    def has_parent(self):
        """
        returnera True om noden har en parent nod, annars False.
        """

        pass



    def is_left_child(self):
        """
        returnera True om noden är left child till sin parent nod, annars False.
        """

        pass



    def is_right_child(self):
        """
        returnera True om noden är right child tills sin parent nod, annars False.
        """

        pass



    def __lt__(self, other):
        """ returnera True om nodens key är mindre än other, annars False. """

        if isinstance(other, Node):
            return self.key < other.key
        else:
            return self.key < other



    def __gt__(self, other):
        """ returnera True om nodens key är större än other, annars False. """

        if isinstance(other, Node):
            return self.key > other.key
        else:
            return self.key > other



    def __eq__(self, other):
        """ returnera True om nodens key är lika med other, annars False. """

        if isinstance(other, Node):
            return self.key == other.key
        else:
            return self.key == other
