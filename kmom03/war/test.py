#!/usr/bin/python3
"""Game of War - unittest - KMOM03"""

import unittest

from card import Card
from deck import Deck
from hand import Hand

class TestDeck(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """

        self.deck = Deck()
        self.deck.build_deck()

    def tearDown(self):
        """ Remove dependencies after test """

        self.deck = None

    def test_created_deck(self):
        """ Check so that new deck consists of 52 cards """

        self.assertIs(len(self.deck.deck), 52)

    def test_created_deck_order(self):
        """ Check order of deck """

        self.assertEqual(repr(self.deck.deck[0]), "Ace of Heart")
        self.assertEqual(repr(self.deck.deck[25]), "King of Spades")
        self.assertEqual(repr(self.deck.deck[51]), "King of Clover")

    def test_shuffled_deck_order(self):
        """ Check so that shuffling a deck works  """

        self.assertEqual(self.deck.shuffled, 0)
        self.deck.shuffle()
        self.assertEqual(self.deck.shuffled, 1)

    def test_splitted_stack(self):
        """ Test so that deck get splitted correctly"""

        deck1, deck2 = self.deck.split_deck()

        self.assertEqual(len(deck1), len(deck2))
        self.assertEqual(len(deck1), 26)


class TestHand(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """

        name = "Patrik"
        hand = ["Ace of Heart", "2 of Spades", "King of Clover", "10 of Diamond"]
        self.hand = Hand(name, hand)


    def tearDown(self):
        """ Remove dependencies after test """

        self.hand = None

    def test_name(self):
        """ Check player name """

        self.assertEqual(self.hand.name, "Patrik")

    def test_player_hand(self):
        """ Check player hand """

        self.assertEqual(self.hand.hand[0], "Ace of Heart")
        self.assertEqual(self.hand.hand[3], "10 of Diamond")

    def test_picking_up_cards(self):
        """ 
        Test so that picked up cards appends to the hand
        5 of Diamond should be first of the new hand
        """

        picked_cards = ["5 of Diamond", "King of Heart", "3 of Spades"]

        self.assertEqual(len(self.hand.hand), 4)
        self.hand.add_card(picked_cards)
        self.assertEqual(len(self.hand.hand), 7)
        self.assertEqual(self.hand.hand[0], "5 of Diamond")

    def test_play_card(self):
        """ Test playing card is the top card of the hand """



if __name__ == "__main__":
    unittest.main()
