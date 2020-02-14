from node import Node


class BinarySearchTree():
    """ .sd. """

    def __init__(self):
        """ ### """

        self.root = None
        self.size = 0



    def insert(self, key, value):
        """ ### """

        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)



    @staticmethod
    def _insert(key, value, node):
        """ ### """

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
        else:
            node.value = value



    def inorder_traversal_print(self):
        """ ### """

        self._print_nodes(self.root)



    @staticmethod
    def _print_nodes(node):
        """ ### """

        if node.has_left_child():
            BinarySearchTree._print_nodes(node.left)
        
        print(node.value)
        
        if node.has_right_child():
            BinarySearchTree._print_nodes(node.right)



    def get(self, key):
        """
        Returnera value från noden med nyckeln key. Om key inte finns i 
        trädet lyft ett KeyError exception (det inbyggda).
        """

        return self._get(self.root, key).value



    @staticmethod
    def _get(node, key):
        """ asdasd """

        if node.key == key:
            return node
        else:
            raise KeyError("No matching key found!")

        if node.has_left_child():
            BinarySearchTree._get(node.left, key)

        if node.has_right_child():
            BinarySearchTree._get(node.right, key)



    def remove(self):
        """ 
        Ta bort nod med samma key, returnera värdet från noden. 
        Om nod med key inte finns lyft KeyError exception (det inbyggda). 
        """

        pass

bst = BinarySearchTree()
bst.insert(8, "first")
bst.insert(4, "second")
bst.insert(11, "third")
#bst.inorder_traversal_print()
print(bst.get(9))
