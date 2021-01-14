import unittest
import mock
from Deck import Deck
from Card import Card


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_length(self):
        self.assertEqual(
            len(self.deck),
            52,
        )

    def test_init_deck_exclude(self):
        deck = Deck(exclude=[Card(rank="Ten", suit="Spade")])
        self.assertEqual(
            str(deck),
            "Deck: 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, JS, QS, KS, AS, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH, AH, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC, AC, 2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD, AD",
        )
        self.assertEqual(len(deck), 51)

        deck = Deck(
            exclude=[Card(rank="Ten", suit="Spade"), Card(rank="Two", suit="Spade")]
        )
        self.assertEqual(
            str(deck),
            "Deck: 3S, 4S, 5S, 6S, 7S, 8S, 9S, JS, QS, KS, AS, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH, AH, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC, AC, 2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD, AD",
        )
        self.assertEqual(len(deck), 50)

    def test_shuffle(self):
        self.assertNotEqual(
            self.deck.shuffle(),
            "Deck: 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, JS, QS, KS, AS, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH, AH, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC, AC, 2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD, AD",
        )
        self.assertEqual(
            len(self.deck),
            52,
        )

    def test_deal(self):
        self.assertEqual(
            str(self.deck.deal()),
            "AD",
        )
        self.assertEqual(
            len(self.deck),
            51,
        )