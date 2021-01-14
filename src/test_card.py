import unittest
import mock
from Card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(rank="Ten", suit="Club")

    def test_get_suit(self):
        self.assertEqual(
            self.card.get_suit(),
            "Club",
        )

    def test_get_rank(self):
        self.assertEqual(
            self.card.get_rank(),
            "Ten",
        )

    def test_get_value(self):
        self.assertEqual(
            Card(rank="Two", suit="Club").get_value(),
            1,
        )
        self.assertEqual(
            Card(rank="Jack", suit="Club").get_value(),
            10,
        )
        self.assertEqual(
            Card(rank="Queen", suit="Club").get_value(),
            11,
        )
        self.assertEqual(Card(rank="King", suit="Club").get_value(), 12)
        self.assertEqual(
            Card(rank="Ace", suit="Club").get_value(),
            13,
        )