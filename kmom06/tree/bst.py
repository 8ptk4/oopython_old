#!/usr/bin/python3
""" Binary Search Tree - KMOM06 """

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
        """ Get value based on matching key """

        if node is None:
            raise KeyError("No matching key found!")

        if node.key == key:
            return node
        elif key < node.key:
            return BinarySearchTree._get(node.left, key)
        elif key > node.key:
            return BinarySearchTree._get(node.right, key)



    def remove(self, key):
        """ Delete node """

        return self._remove(BinarySearchTree._get(self.root, key))



    @staticmethod
    def _remove(node):
        """ Delete node """

        node_to_return = node.value

        # Case 1 (node has no children)
        if node.has_left_child() and node.has_right_child() is None:
            if node == BinarySearchTree.root:
                BinarySearchTree.root = None
            elif node.is_left_child():
                node.parent.left = None
            node.parent.right = None

        # Case 2 (node has two children)
        elif node.has_both_children():
            successor = BinarySearchTree._find_successor(node.right)
            node.key = successor.key
            node.value = successor.value
            if successor.is_left_child():
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right

        # Case 3 (node has left child)
        elif node.has_left_child() and node.has_parent():
            if node.is_left_child():
                node.parent.left = node.left
            else:
                node.parent.right = node.left

            BinarySearchTree.root = node.left

        # Case 4 (node has right child)
        elif node.has_right_child() and node.has_parent():
            if node.is_left_child():
                node.parent.left = node.right
            else:
                node.parent.right = node.right

            BinarySearchTree.root = node.right

        return node_to_return



    @staticmethod
    def _find_successor(successor):
        """ return successor """
        if successor.left is None:
            return successor
        return BinarySearchTree._find_successor(successor.left)
