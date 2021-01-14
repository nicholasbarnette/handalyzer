import unittest
import mock
from Player import Player
from Card import Card


class TestPlayer(unittest.TestCase):
    def test_add_card(self):
        player = Player(0)
        self.assertEqual(
            player.add_card(Card(rank="Ten", suit="Club")),
            True,
        )
        self.assertEqual(
            player.add_card(Card(rank="Eight", suit="Club")),
            True,
        )
        self.assertEqual(
            player.add_card(Card(rank="Nine", suit="Club")),
            False,
        )

    def test_get_hand(self):
        c1 = Card(rank="Ten", suit="Club")
        c2 = Card(rank="Eight", suit="Club")
        player = Player(0)
        player.add_card(c1)
        player.add_card(c2)
        a = []
        for c in player.get_hand():
            a.append(str(c))
        self.assertSequenceEqual(a, [str(c1), str(c2)])

    def test_get_id(self):
        player = Player(0)
        self.assertEqual(player.get_id(), 0)

    def test_init_hand(self):
        c1 = Card(rank="Ten", suit="Club")
        c2 = Card(rank="Eight", suit="Club")
        c3 = Card(rank="Six", suit="Club")
        player = Player(0, [])
        self.assertSequenceEqual(
            player.get_hand(),
            [],
        )

        player = Player(0, [c1])
        a = []
        for c in player.get_hand():
            a.append(str(c))
        self.assertSequenceEqual(
            a,
            [str(c1)],
        )

        player = Player(0, [c1, c2])
        a = []
        for c in player.get_hand():
            a.append(str(c))
        self.assertSequenceEqual(
            a,
            [str(c1), str(c2)],
        )

        player = Player(
            0,
            [c1, c2, c3],
        )
        a = []
        for c in player.get_hand():
            a.append(str(c))
        self.assertSequenceEqual(
            a,
            [str(c1), str(c2)],
        )
