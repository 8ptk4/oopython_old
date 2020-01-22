#!/usr/bin/python3
"""Game of War - KMOM03"""

from deck import Deck

class Hand:
    """CLASS HAND"""

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def show_name(self):
        """Return name of the player"""

        return self.name

    def add_card(self, added_cards):
        """Add cards to the hand, add them to the bottom"""

        self.hand[:0] = added_cards

    def remove_card(self):
        """Remove card from hand, aka played card"""
        return self.hand.pop()

    def remaining_cards(self):
        """Remaining cards on hand, displayed in numbers"""

        return str(len(self.hand))
