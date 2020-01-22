#!/usr/bin/python3
"""Game of War - KMOM03"""
from deck import Deck
from hand import Hand


class War:
    """DOCSTRING FOR HAPPINESS"""
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

    def cards_on_hand(self):
        if len(self.player.hand) == 0:
            # skriva ut lite statistic över spelet som gått...
            print("PLAYER LOSED!")
            return False
        elif len(self.computer.hand) == 0:
            # skriva ut lite statistic över spelet som gått...
            print("Computer losed")
            return False
        
        return True

    def start(self):
        round = 0
        while self.cards_on_hand():
            round += 1

            print("Round {}".format(round))
            print("---------------------------------------------------------------")

            player_removed_card = self.player.remove_card()
            self.card_stack_player.append(player_removed_card)

            print("{} draws {}".format(self.player.name, player_removed_card))

            print("{} has {} cards left on hand".format(self.player.name, self.player.remaining_cards()))
            print("")

            computer_removed_card = self.computer.remove_card()
            self.card_stack_computer.append(computer_removed_card)

            print("{} draws {}".format(self.computer.name, computer_removed_card))
            print("{} has {} cards left on hand".format(self.computer.name, self.computer.remaining_cards()))
            print("---------------------------------------------------------------")

            if str(player_removed_card).split(" ")[-1] == str(computer_removed_card).split(" ")[-1]:
                if int(self.card_value(str(player_removed_card).split(" ")[0])) > int(self.card_value(str(computer_removed_card).split(" ")[0])):
                    self.take_stacks("player")
                    self.score(self.player.name)

                    input("Press any key for next round...\n")
                elif int(self.card_value(str(player_removed_card).split(" ")[0])) < int(self.card_value(str(computer_removed_card).split(" ")[0])):
                    self.take_stacks("computer")
                    self.score(self.computer.name)

                    input("Press any key for next round...\n")
            else:
                input("\nPress any key for next round...\n")

if __name__ == "__main__":
    War()