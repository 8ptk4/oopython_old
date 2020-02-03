#!/usr/bin/python3
""" Unordered list - KMOM04 """

import sys
from unorderedlist import UnorderedList
from errors import IndexErrorException
from errors import ValueErrorException
from errors import AttributeErrorException
from sort import insertion_sort
from sort import bubble_sort

class Handler:
    """ Handler class """



    def __init__(self):
        """ Initialize Unordered List class and start"""

        self.my_list = UnorderedList()
        self.start()



    def start(self):
        """ Start """ 

        while True:
            print("""
[1] Check if the list is empty
[2] Add value last in list
[3] Insert value at a specific index
[4] Replace value at a specific index
[5] Show size of list
[6] Show value at a specific index
[7] Show index of a specific value
[8] Show all values in the list
[9] Remove node that match value
[10] Sort list with Insertion Sort
[11] Sort list with Bubble Sort
[exit] Exit
            """)
            val = input('Choice: \n>>> ')

            if val == "1":
                print("\nCheck if the list is empty:")
                print(self.my_list.is_empty())

            elif val == "2":
                print("\nAdd value last in list:")
                data = input("Value: ")
                self.my_list.add(data)

            elif val == "3":
                print("\nInsert value at a specific index:")
                index = input("Index: ")
                data = input("Value: ")

                try:
                    self.my_list.insert(int(index), data)
                except IndexErrorException as e:
                    print(e)

            elif val == "4":
                print("\nReplace value at a specific index:")
                index = input("Index: ")
                data = input("Value: ")

                try:
                    self.my_list.set(int(index), data)
                except IndexErrorException as e:
                    print(e)

            elif val == "5":
                print("\nShow size of list:")
                res = self.my_list.size()
                print(res)

            elif val == "6":
                print("\nShow value at a specific index:")
                data = input("Index: ")

                try:
                    res = self.my_list.get(int(data))
                    print(res)
                except IndexErrorException as e:
                    print(e)

            elif val == "7":
                print("\nShow index by value:")
                data = input("Value: ")

                try:
                    res = self.my_list.index_of(data)
                    print(res)
                except ValueErrorException as e:
                    print(e)

            elif val == "8":
                print("\nShow all values in the list:")
                
                res = self.my_list.print_list()

                print(res)

            elif val == "9":
                print("\nRemove node by value:")
                data = input("Value: ")

                try:
                    self.my_list.remove(data)
                except ValueErrorException as e:
                    print(e)

            elif val == "10":
                print("Sort list with Insertion Sort")
                res = self.my_list.print_list()
                insertion = insertion_sort(res)

                print(insertion)
            
            elif val == "11":
                print("Sort list with Bubble Sort")
                res = self.my_list.print_list()
                bubble = bubble_sort(res)
                
                print(bubble)
    
            elif val == "exit":
                sys.exit()

            else:
                print("No choice that match! try again")

if __name__ == "__main__":
    Handler()
