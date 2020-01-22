#!/usr/bin/python3
"""Game of War - KMOM03"""

import random
from card import Card

class Deck:
    """CLASS DECK"""

    def __init__(self):
        self.deck = []

    def shuffle(self):
        """Shuffles card deck"""

        random.shuffle(self.deck)

    def build_deck(self):
        """Creates deck with 52 cards"""

        for suit in range(4):
            for value in range(1, 14):
                self.deck.append(Card(value, suit))

    def split_deck(self):
        """Split deck in half"""

        return (self.deck[:26], self.deck[26:])
