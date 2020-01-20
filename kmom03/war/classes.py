import random

class Card:
    names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
    "Queen", "King"]
    suits = ["Heart", "Spades", "Diamond", "Clover"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "{} {}".format(self.names[self.value], self.suits[self.suit])

class Deck:
    def __init__(self):
        self.cards = []
        self.reset_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.insert(0, card)

    def reset_cards(self):
        self.cards = []
        for suit in range(4):
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

if __name__ == "__main__":
    c = Card(1,1)
    d = Deck()
    # d.shuffle()
    c = d.take_card()
    d.add_card(c)
    print(d.cards[0])