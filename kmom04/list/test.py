#!/usr/bin/python3
""" Unordered list - unittest - KMOM04 """

import unittest
from unorderedlist import UnorderedList
from errors import IndexErrorException
from errors import ValueErrorException

class TestUnorderedList(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """



    def setUp(self):
        """ Create object for all tests """

        self.unordered_list = UnorderedList()
        self.unordered_list.add("Patrik")
        self.unordered_list.add("Karlsson")



    def tearDown(self):
        """ Remove dependencies after test """

        self.unordered_list = None



    def test_insert(self):
        """ Test method insert """
        # List looks like this 0: Patrik 1: Karlsson

        # Trying to insert new value at index 3 and -1 should raise exception
        self.assertRaises(IndexErrorException,
                          self.unordered_list.insert, int(3), "test")
        self.assertRaises(IndexErrorException,
                          self.unordered_list.insert, int(-1), "test")

        # Trying to insert new value at index 0 should work and not raise
        # exception
        self.unordered_list.insert(int(0), "test")
        # 0: test 1: Patrik 2: Karlsson

        # Trying to insert new value at index 3 should work and not raise
        # exception
        self.unordered_list.insert(int(3), "test2")
        # 0: test 1: Patrik 2: Karlsson 3: test2

        # Check if index 0 == test and index 3 = test2
        self.assertEqual(self.unordered_list.get(int(0)), "test")
        self.assertEqual(self.unordered_list.get(int(3)), "test2")



    def test_set(self):
        """ Test method set """

        # Trying to replace new value at index 2 or -1 should raise exception
        self.assertRaises(IndexErrorException,
                          self.unordered_list.set, int(2), "test")
        self.assertRaises(IndexErrorException,
                          self.unordered_list.set, int(-1), "test")

        # Replace a valid index value and check so that the value = new value
        self.unordered_list.set(int(0), "test")
        self.assertEqual(self.unordered_list.get(0), "test")



    def test_get(self):
        """ Test method get """

        # Trying to get value at index 2 or -1 should raise exception
        self.assertRaises(IndexErrorException, self.unordered_list.get, int(2))
        self.assertRaises(IndexErrorException, self.unordered_list.get, int(-1))

        # Test get value at indec 0 and 1 should return Patrik and Karlsson
        self.assertEqual(self.unordered_list.get(int(0)), "Patrik")
        self.assertEqual(self.unordered_list.get(int(1)), "Karlsson")



    def test_index_of(self):
        """ Test index_of method """

        # Trying to get value at index 2 or -1 should raise exception
        self.assertRaises(ValueErrorException,
                          self.unordered_list.index_of, "Patrik_test")
        self.assertRaises(ValueErrorException,
                          self.unordered_list.index_of, "Karlsson_test")

        # Test get index for Patrik and Karlsson should return 0 and 1
        self.assertEqual(self.unordered_list.index_of("Patrik"), 0)
        self.assertEqual(self.unordered_list.index_of("Karlsson"), 1)



    def test_remove(self):
        """ Test remove method """

        # Trying to remove a value that doesnt exist should raise exception
        self.assertRaises(ValueErrorException,
                          self.unordered_list.remove, "test")

        # Before removing items in list should be 2
        self.assertEqual(self.unordered_list.size(), 2)
        self.unordered_list.remove("Patrik")
        # After removing items in list should be 1
        self.assertEqual(self.unordered_list.size(), 1)
        # After removing last item in list, the list shall be emtpy
        self.unordered_list.remove("Karlsson")
        self.assertEqual(self.unordered_list.is_empty(), True)


if __name__ == "__main__":
    unittest.main()
