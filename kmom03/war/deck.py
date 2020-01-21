import random
from card import Card

class Deck:
    def __init__(self):
        self.deck = []

    def shuffle(self):
        random.shuffle(self.deck)

    def build_deck(self):
        self.deck = []
        for suit in range(4):
            for value in range(1, 14):
                self.deck.append(Card(value, suit))
    
    def split_deck(self):
        return (self.deck[:26], self.deck[26:])