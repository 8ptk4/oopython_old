from node import Node


class BinarySearchTree():
    """ BinarySearchTree class """



    def __init__(self):
        """ Initialize BinarySearchTree """

        self.root = None
        self.size = 0



    def insert(self, key, value, node):
        """  
        Skapar en ny nod med key och value,. ägger till en noden på rätt plats i trädet, baserat på key.
        """ 

        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)



    @staticmethod
    def _insert(key, value, node):
        if key < node:
            if node.has_left_child():
                BinarySearchTree._insert(key, value, node.left)
            else:
                node.left = Node(key, value, node)
        elif key > node:
            if node.has_right_child():
                BinarySearchTree._insert(key, value, node.right)
            else:
                node.right = Node(key, value, node)
        elif key == node:
            node.value == value



    def inorder_traversal_print(self):
        """ 
        Skriver ut en noderna i trädet i rätt ordning, lågt till högt.
        """
        pass 



    def get(self, key): # Node.value
        """
        Returnera value från noden med nyckeln key. Om key inte finns i trädet lyft ett KeyError exception (det inbyggda).
        """ 
        pass



    def remove(self, key): # Node.value
        """
        Ta bort nod med samma key, returnera värdet från noden. Om nod med key inte finns lyft KeyError exception (det inbyggda).
        """
        pass
