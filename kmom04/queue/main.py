#!/usr/bin/python3
""" Queue - Kmom04 """

import sys
from queue import Queue
from errors import EmptyQueueException



class Handler:
    """ Handler class """



    def __init__(self):
        """ Initialize class """

        self.my_list = Queue()
        self.start()



    def start(self):
        """ Start method """

        while True:
            print("""
[1] Add a value
[2] Remove the next value
[3] Look at the current value
[4] Look at the next value
[5] Size    
[6] Empty ?
[7] List all values

[exit] Exit
            """)
            val = input('What do you want to do ? \n>>> ')

            if val == "1":
                print("\nAdd a value:")
                value = input(">>> ")
                self.my_list.enqueue(value)

            elif val == "2":
                print("\nRemove the next value:\n")
                self.my_list.dequeue()

            elif val == "3":
                print("\nLook at the current value:\n")

                try:
                    print(self.my_list.peek_current())
                except EmptyQueueException as e:
                    print(e)

            elif val == "4":
                print("\nLook at the next value\n")

                try:
                    print(self.my_list.peek())
                except EmptyQueueException as e:
                    print(e)

            elif val == "5":
                print("\nSize\n")
                print(self.my_list.size())

            elif val == "6":
                print("\nEmpty ?\n")
                print(self.my_list.is_empty())

            elif val == "7":
                print("\nList all values\n")

                try:
                    self.my_list.traverse()
                except EmptyQueueException as e:
                    print(e)

            elif val == "exit":
                sys.exit()

            else:
                print("Finns inget val för detta buuuu")

if __name__ == "__main__":
    Handler()
