#!/usr/bin/python3
""" Insertion sort - KMOM05 """

def insertion_sort(lst):
    """ Insertion sort """

    head = lst.head
    current_node = head

    while current_node.next is not None:

        if current_node.next.data > current_node.data:
            current_node = current_node.next

        else:
            temp = current_node.next
            current_node.next = temp.next

            if head.data > temp.data:
                temp.next = head
                lst.head = temp
                head = lst.head

            else:
                inpos = head

                while temp.data > inpos.next.data:
                    inpos = inpos.next

                temp.next = inpos.next
                inpos.next = temp



def bubble_sort(lst):
    """ Bubble sort """

    head = lst.head
    swap = 0

    if head is not None:

        while 1:
            swap = 0
            tmp = head

            while tmp.next is not None:

                if tmp.data > tmp.next.data:
                    swap += 1
                    p = tmp.data
                    tmp.data = tmp.next.data
                    tmp.next.data = p
                    tmp = tmp.next

                else:
                    tmp = tmp.next

            if swap == 0:
                break

            else:
                continue
