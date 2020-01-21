from deck import Deck

class Hand:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def show_name(self):
        return self.name

    # def add_card(self, added_cards):
    #    self.cards.extend(added_cards)
    
    # def remove_card(self):
    #    return self.cards.pop()

    def show_hand(self):
        return "{}".format(self.hand)
        # print(self.name, self.hand)

