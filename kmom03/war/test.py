import unittest
from classes import Card, Deck

class TestCard(unittest.TestCase):

    def test_a_card_instance(self):
        """Test that a Card object is of Card instance"""
        c = Card(1, 1)
        self.assertIsInstance(c, Card)

    def test_b_card_str(self):
        """Test magic str method"""
        c = Card(3, 2)
        self.assertEqual(str(c), "3 Diamond")

    def test_c_value_to_big(self):
        """Should raise ValueError if over 13"""
        with self.assertRaises(ValueError):
            Card(15, 3)

if __name__ == "__main__":
    unittest.main()