from card import Card
from deck import Deck
from hand import Hand
import random
import time

class War:
    def __init__(self):
        self.card_stack_player = []
        self.card_stack_computer = []
        self.introduction()
        self.initiate_deck()
        self.initiate_players()
        self.start()

    def initiate_deck(self):
        deck = Deck()
        deck.build_deck()
        deck.shuffle()
        self.deck1, self.deck2 = deck.split_deck()

    def initiate_players(self):
        self.computer = Hand("Computer", self.deck1)
        name = input("\nWhat is your name:\n>>> ")
        print("")
        self.player = Hand(name, self.deck2)
        
    def card_value(self, value):
        switcher = {
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14
        }
        
        return int(switcher.get(value, value))
    
    def take_stacks(self, player):
        self.collected_stack = self.card_stack_player + self.card_stack_computer
        if player == "player":
            self.player.add_card(self.collected_stack)
            
        else:
            self.computer.add_card(self.collected_stack)
            
        
    def score(self, player):
        self.card_stack_player[:] = []
        self.card_stack_computer[:] = []
        print("\n>>> {} won and this round picked upp {} cards <<<\n".format(player, len(self.collected_stack)))

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
        input("\nPress any key to start...")

    def start(self):
        round = 0
        while True:
            round += 1

            print("Round {}".format(round))
            print("---------------------------------------------------------------")
            time.sleep(0.5)

            player_removed_card = self.player.remove_card()
            self.card_stack_player.append(player_removed_card)

            print("{} draws {}".format(self.player.name, player_removed_card))
            time.sleep(0.5)
            print("{} has {} cards left on hand".format(self.player.name, self.player.remaining_cards()))
            print("")
            time.sleep(0.5)

            computer_removed_card = self.computer.remove_card()
            self.card_stack_computer.append(computer_removed_card)

            print("{} draws {}".format(self.computer.name, computer_removed_card))
            print("{} has {} cards left on hand".format(self.computer.name, self.computer.remaining_cards()))
            print("---------------------------------------------------------------")
            time.sleep(0.5)

            if str(player_removed_card).split(" ")[-1] == str(computer_removed_card).split(" ")[-1]:
                if int(self.card_value(str(player_removed_card).split(" ")[0])) > int(self.card_value(str(computer_removed_card).split(" ")[0])):
                    self.take_stacks("player")
                    self.score(self.player.name)
                    print("##############")
                    print("test")
                    print("player dragna", self.card_stack_player)
                    print("player hand", self.player.hand)
                    print("computer dragna", self.card_stack_computer)
                    print("computer hand", self.computer.hand)
                    print("##############")
                    input("Press any key for next round...")
                elif int(self.card_value(str(player_removed_card).split(" ")[0])) < int(self.card_value(str(computer_removed_card).split(" ")[0])):
                    self.take_stacks("computer")
                    self.score(self.computer.name)
                    print("##############")
                    print("test")
                    print("player dragna", self.card_stack_player)
                    print("player hand", self.player.hand)
                    print("computer dragna", self.card_stack_computer)
                    print("computer hand", self.computer.hand)
                    print("##############")
                    input("Press any key for next round...")
            else:
                print("##############")
                print("test")
                print("player dragna", self.card_stack_player)
                print("player hand", self.player.hand)
                print("computer dragna", self.card_stack_computer)
                print("computer hand", self.computer.hand)
                print("##############")
                input("\nPress any key for next round...\n")
War()

# SKriva ut och kolla så dragna korten hamnar rätt i vinnaraens hand.
# Fixa while loopen så den känner av när en spelare har slut på kort i handen
# Utse vinnare 