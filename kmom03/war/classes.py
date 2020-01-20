class Card:
    names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
    "Queen", "King"]
    suits = ["Heart", "Spades", "Diamond", "Clover"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "{} {}".format(self.names[self.value], self.suits[self.suit])

if __name__ == "__main__":
    c = Card(1,1)
    print(c)