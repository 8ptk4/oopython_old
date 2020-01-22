#!/usr/bin/python3
"""Game of War - KMOM03"""

from deck import Deck

class Hand:
    """CLASS HAND"""

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def show_name(self):
        return self.name

    def add_card(self, added_cards):
        self.hand[:0] = added_cards

    def remove_card(self):
        return self.hand.pop()

    def remaining_cards(self):
        return str(len(self.hand))

    def show_hand(self):
        return "{}".format(self.hand)

