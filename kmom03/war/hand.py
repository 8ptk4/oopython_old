from deck import Deck

class Hand:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def show_name(self):
        return self.name

    def add_card(self, added_cards):
        self.hand.extend(added_cards)
    
    def remove_card(self):
        return self.hand.pop()

    def remaining_cards(self):
        return str(len(self.hand))

    def show_hand(self):
        return "{}".format(self.hand)

