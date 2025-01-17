#!/usr/bin/python3
"""Game of War - KMOM03"""

class Card:
    """CARD CLASS"""

    names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
             "Queen", "King"]
    suits = ["Heart", "Spades", "Diamond", "Clover"]

    def __init__(self, value, suit):
        if value > 13:
            raise ValueError
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.names[self.value], self.suits[self.suit])
