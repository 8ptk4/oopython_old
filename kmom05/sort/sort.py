#!/usr/bin/python3
""" Insertion sort - KMOM05 """

def insertion_sort(items):
    """ Insertion sort """

    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1

    return items



def bubble_sort(items):
    """ Bubble sort """

    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items
