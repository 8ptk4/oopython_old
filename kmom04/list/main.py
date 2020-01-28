#!/usr/bin/python3

import sys
from unorderedlist import UnorderedList
from errors import IndexErrorException
from errors import ValueErrorException

class Handler:
    """
    Handler class
    """

    def __init__(self):
        """ Initialize Unordered List class and start"""

        self.my_list = UnorderedList()
        self.start()

    def frame(self, output):
        print("---------------------------------------------------------------")
        print(output)
        print("---------------------------------------------------------------")
    
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
[exit] Exit
            """)
            val = input('What do you want to do ? \n>>> ')

            if val == "1":
                print("\nCheck if the list is empty:")
                res = self.my_list.is_empty()
                self.frame(res)
            elif val == "2":
                print("\nAdd value last in list:")
                data = input(">>> ")
                self.frame("{} added to the list!".format(data))
                self.my_list.add(data)
            elif val == "3":
                print("\nInsert value at a specific index:\n")
                #try:
                 #   print(self.myList.peek_current())
                #except EmptyQueueException as e:
                 #   print(e)
            elif val == "4":
                print("\nReplace value at a specific index\n")
                #try:
                 #   print(self.myList.peek())
                #except EmptyQueueException as e:
                 #   print(e)
            elif val == "5":
                print("\nShow size of list")
                res = self.my_list.size()
                self.frame(res)
            elif val == "6":
                print("\nShow value at a specific index\n")
                data = input(">>> ")
                try:
                    res = self.my_list.get(data)
                    print(res)
                except IndexErrorException as e:
                    print(e)
            elif val == "7":
                print("\nShow index of a specific value\n")
                data = input(">>> ")
                try:
                    res = self.my_list.index_of(data)
                    self.frame(res)
                except ValueErrorException as e:
                    self.frame(e)
            elif val == "8":
                print("\nShow all values in the list")
                print("---------------------------------------------------------------")
                self.my_list.print_list()
                print("\n---------------------------------------------------------------")
            elif val == "9":
                print("\nRemove node that match value\n")
                data = input(">>> ")
                try:
                    self.my_list.remove(data)
                    self.frame("{} removed from the list!".format(data))
                except ValueErrorException as e:
                    self.frame(e)
            elif val == "exit":
                sys.exit()
            else:
                self.frame("No choice that match! try again")


if __name__ == "__main__":
    Handler()
