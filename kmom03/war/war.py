from card import Card
from deck import Deck
from hand import Hand
import random
import time

class War:
    def __init__(self):
        self.card_stack = []
        self.introduction()
        self.initiate_deck()
        self.initiate_players()
        self.rotation()
        self.start()

    def initiate_deck(self):
        deck = Deck()
        deck.build_deck()
        deck.shuffle()
        self.deck1, self.deck2 = deck.split_deck()

    def initiate_players(self):
        self.computer = Hand("Computer", self.deck1)
        name = input("What is your name:\n>>> ")
        self.player = Hand(name, self.deck2)

    def rotation(self):
        self.rand = random.randint(1, 2)
        print("")
        print("Checking who will start...")
        time.sleep(1.1)
        if self.rand == 1:
            self.player1 = self.computer
            self.player2 = self.player
            print(self.player1.name, "starts the game")
            print("")
        elif self.rand == 2:
            self.player1 = self.player
            self.player2 = self.computer
            print(self.player1.name, "starts the game")
            print("")

    def introduction(self):
        print("""
 █     █░ ▄▄▄       ██▀███  
▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒
▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒
░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  
░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒
░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░
  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░
  ░   ░    ░   ▒     ░░   ░ 
    ░          ░  ░   ░   
        """)
        input("Press any key to start...")
        print("")

    def start(self):
        
        print(self.player1.show_hand())
        print(self.player2.show_hand())

War()
