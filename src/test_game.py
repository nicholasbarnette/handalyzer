import unittest
import mock
from Game import Game
from Card import Card


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_is_royal_flush(self):
        self.assertEqual(
            self.game._is_royal_flush(
                [
                    Card("Two", "Diamond"),
                    Card("Three", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("Jack", "Diamond"),
                    Card("Ten", "Diamond"),
                    Card("Ace", "Diamond"),
                    Card("King", "Diamond"),
                ],
            ),
            False,
        )
        self.assertEqual(
            self.game._is_royal_flush(
                [
                    Card("Two", "Diamond"),
                    Card("King", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("Jack", "Diamond"),
                    Card("Ten", "Diamond"),
                    Card("Ace", "Diamond"),
                    Card("Three", "Diamond"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_royal_flush(
                [
                    Card("King", "Diamond"),
                    Card("Two", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("Jack", "Diamond"),
                    Card("Ten", "Diamond"),
                    Card("Ace", "Diamond"),
                    Card("Three", "Diamond"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_royal_flush(
                [
                    Card("Ace", "Diamond"),
                    Card("King", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("Jack", "Diamond"),
                    Card("Ten", "Diamond"),
                    Card("Two", "Diamond"),
                    Card("Three", "Diamond"),
                ],
            ),
            True,
        )

    def test_is_straight_flush(self):
        self.assertEqual(
            self.game._is_straight_flush(
                [
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Six", "Spade"),
                    Card("Ten", "Spade"),
                    Card("Ace", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_straight_flush(
                [
                    Card("Ten", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Six", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_straight_flush(
                [
                    Card("Eight", "Spade"),
                    Card("Nine", "Spade"),
                    Card("Ten", "Spade"),
                    Card("Jack", "Spade"),
                    Card("Queen", "Spade"),
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_straight_flush(
                [
                    Card("Eight", "Spade"),
                    Card("Nine", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Jack", "Spade"),
                    Card("Queen", "Spade"),
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                ]
            ),
            False,
        )
        self.assertEqual(
            self.game._is_straight_flush(
                [
                    Card("Eight", "Spade"),
                    Card("Nine", "Spade"),
                    Card("Ten", "Spade"),
                    Card("Jack", "Spade"),
                    Card("King", "Spade"),
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                ]
            ),
            False,
        )

    def test_is_four_of_kind(self):
        self.assertEqual(
            self.game._is_four_of_kind(
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Nine", "Spade"),
                ],
            ),
            False,
        )
        self.assertEqual(
            self.game._is_four_of_kind(
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Ten", "Club"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Nine", "Spade"),
                ],
            ),
            False,
        )
        self.assertEqual(
            self.game._is_four_of_kind(
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Ten", "Club"),
                    Card("Ten", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Nine", "Spade"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_four_of_kind(
                [
                    Card("Ten", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Ten", "Club"),
                    Card("Ten", "Heart"),
                    Card("Seven", "Spade"),
                    Card("Nine", "Spade"),
                ],
            ),
            True,
        )

    def test_is_full_house(self):
        self.assertEqual(
            self.game._is_full_house(
                [
                    Card("Three", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Three", "Heart"),
                    Card("Two", "Spade"),
                    Card("Two", "Heart"),
                    Card("Seven", "Spade"),
                    Card("Nine", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_full_house(
                [
                    Card("Three", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Four", "Heart"),
                    Card("Two", "Spade"),
                    Card("Two", "Heart"),
                    Card("Seven", "Spade"),
                    Card("Nine", "Spade"),
                ]
            ),
            False,
        )
        self.assertEqual(
            self.game._is_full_house(
                [
                    Card("Three", "Spade"),
                    Card("Three", "Diamond"),
                    Card("Four", "Heart"),
                    Card("Two", "Spade"),
                    Card("Two", "Heart"),
                    Card("Seven", "Spade"),
                    Card("Three", "Heart"),
                ]
            ),
            False,
        )
        self.assertEqual(
            self.game._is_full_house(
                [
                    Card("Three", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Three", "Heart"),
                    Card("Two", "Spade"),
                    Card("Four", "Heart"),
                    Card("Seven", "Spade"),
                    Card("Nine", "Spade"),
                ]
            ),
            False,
        )

    def test_is_flush(self):
        self.assertEqual(
            self.game._is_flush(
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Six", "Spade"),
                    Card("Nine", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_flush(
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Six", "Diamond"),
                    Card("Nine", "Diamond"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_flush(
                [
                    Card("Ten", "Diamond"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Six", "Spade"),
                    Card("Nine", "Diamond"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_flush(
                [
                    Card("Ten", "Diamond"),
                    Card("Five", "Diamond"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Six", "Spade"),
                    Card("Nine", "Diamond"),
                ]
            ),
            False,
        )

    def test_is_straight(self):
        self.assertEqual(
            self.game._is_straight(
                [
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Six", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_straight(
                [
                    Card("Eight", "Spade"),
                    Card("Nine", "Diamond"),
                    Card("Ten", "Spade"),
                    Card("Jack", "Spade"),
                    Card("Queen", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_straight(
                [
                    Card("Two", "Diamond"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ]
            ),
            False,
        )

    def test_is_three_of_kind(self):
        self.assertEqual(
            self.game._is_three_of_kind(
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Ten", "Club"),
                    Card("King", "Heart"),
                    Card("Ace", "Spade"),
                    Card("King", "Diamond"),
                    Card("Ace", "Club"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_three_of_kind(
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("King", "Diamond"),
                    Card("Ace", "Club"),
                ],
            ),
            False,
        )

    def test_is_two_pair(self):
        self.assertEqual(
            self.game._is_two_pair(
                [
                    Card("Ten", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Two", "Club"),
                    Card("Ten", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Club"),
                    Card("Nine", "Club"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_two_pair(
                [
                    Card("Ten", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Two", "Club"),
                    Card("Ten", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Club"),
                    Card("Nine", "Club"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_two_pair(
                [
                    Card("Ten", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Club"),
                    Card("Nine", "Club"),
                ],
            ),
            False,
        )

    def test_is_pair(self):
        self.assertEqual(
            self.game._is_pair(
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Two", "Club"),
                    Card("King", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_pair(
                [
                    Card("Ten", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Two", "Club"),
                    Card("King", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            True,
        )
        self.assertEqual(
            self.game._is_pair(
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            False,
        )

    def test_find_duplicates(self):
        self.assertEqual(
            self.game._find_duplicates(
                3,
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            0,
        )
        self.assertEqual(
            self.game._find_duplicates(
                9,
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            1,
        )
        self.assertEqual(
            self.game._find_duplicates(
                9,
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            2,
        )
        self.assertEqual(
            self.game._find_duplicates(
                9,
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Ten", "Club"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            3,
        )
        self.assertEqual(
            self.game._find_duplicates(
                9,
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Ten", "Club"),
                    Card("Ten", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Diamond"),
                    Card("King", "Spade"),
                ],
            ),
            4,
        )

    def test_get_highest_card(self):
        self.assertEqual(
            self.game._get_highest_card(
                [
                    Card("Ten", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Two", "Club"),
                    Card("Ten", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Eight", "Heart"),
                    Card("King", "Spade"),
                ],
            ),
            9,
        )
        self.assertEqual(
            self.game._get_highest_card(
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Two", "Club"),
                    Card("Ten", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Eight", "Heart"),
                    Card("King", "Spade"),
                ],
            ),
            9,
        )
        self.assertEqual(
            self.game._get_highest_card(
                [
                    Card("Two", "Spade"),
                    Card("Ten", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Three", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Eight", "Heart"),
                    Card("King", "Spade"),
                ],
            ),
            9,
        )

    def test_insert_ordered(self):
        self.assertSequenceEqual(
            self.game._insert_ordered([], {"id": 0, "value": 55}),
            [{"id": 0, "value": 55}],
        )
        self.assertSequenceEqual(
            self.game._insert_ordered([{"id": 0, "value": 55}], {"id": 0, "value": 58}),
            [{"id": 0, "value": 58}, {"id": 0, "value": 55}],
        )
        self.assertSequenceEqual(
            self.game._insert_ordered([{"id": 0, "value": 55}], {"id": 0, "value": 52}),
            [{"id": 0, "value": 55}, {"id": 0, "value": 52}],
        )
        self.assertSequenceEqual(
            self.game._insert_ordered(
                [
                    {"id": 0, "value": 55},
                    {"id": 0, "value": 52},
                    {"id": 0, "value": 51},
                ],
                {"id": 0, "value": 53},
            ),
            [
                {"id": 0, "value": 55},
                {"id": 0, "value": 53},
                {"id": 0, "value": 52},
                {"id": 0, "value": 51},
            ],
        )

    def test_find_outcome(self):
        game = Game()
        game.deal()
        self.assertEqual(len(game.find_outcome()), len(game.players))

    def test_calculate_straight_value(self):
        self.assertEqual(
            self.game._calculate_straight_value(
                [
                    Card("Eight", "Spade"),
                    Card("Nine", "Diamond"),
                    Card("Ten", "Spade"),
                    Card("Jack", "Spade"),
                    Card("Queen", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ]
            ),
            45,
        )
        self.assertEqual(
            self.game._calculate_straight_value(
                [
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Six", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ]
            ),
            25,
        )
        self.assertEqual(
            self.game._calculate_straight_value(
                [
                    Card("Two", "Diamond"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ]
            ),
            0,
        )

    def test_determine_hand_value(self):
        game = Game()
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("Ace", "Diamond"),
                    Card("King", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("Jack", "Diamond"),
                    Card("Ten", "Diamond"),
                    Card("Two", "Diamond"),
                    Card("Three", "Diamond"),
                ],
            ),
            {"id": "0", "type": "royal_flush", "value": 55},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("King", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("Jack", "Diamond"),
                    Card("Ten", "Diamond"),
                    Card("Nine", "Diamond"),
                    Card("Two", "Diamond"),
                    Card("Three", "Diamond"),
                ],
            ),
            {"id": "0", "type": "straight_flush", "value": 50},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("King", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("King", "Spade"),
                    Card("King", "Heart"),
                    Card("Nine", "Diamond"),
                    Card("King", "Club"),
                    Card("Three", "Diamond"),
                ],
            ),
            {"id": "0", "type": "four_kind", "value": 12},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("King", "Diamond"),
                    Card("Queen", "Diamond"),
                    Card("King", "Spade"),
                    Card("King", "Heart"),
                    Card("Nine", "Diamond"),
                    Card("Queen", "Club"),
                    Card("Three", "Diamond"),
                ],
            ),
            {"id": "0", "type": "full_house", "value": 12},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("Ten", "Spade"),
                    Card("Five", "Spade"),
                    Card("Eight", "Spade"),
                    Card("Two", "Spade"),
                    Card("Ace", "Spade"),
                    Card("Six", "Spade"),
                    Card("Nine", "Spade"),
                ],
            ),
            {"id": "0", "type": "flush", "value": 47},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Club"),
                    Card("Five", "Club"),
                    Card("Six", "Club"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ],
            ),
            {"id": "0", "type": "straight", "value": 25},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("Ten", "Spade"),
                    Card("Ten", "Diamond"),
                    Card("Ten", "Club"),
                    Card("King", "Heart"),
                    Card("Ace", "Spade"),
                    Card("King", "Diamond"),
                    Card("Ace", "Club"),
                ],
            ),
            {"id": "0", "type": "three_kind", "value": 9},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("Ten", "Spade"),
                    Card("Two", "Diamond"),
                    Card("Two", "Club"),
                    Card("Ten", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Club"),
                    Card("Nine", "Club"),
                ],
            ),
            {"id": "0", "type": "two_pair", "value": 9},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("Six", "Spade"),
                    Card("Three", "Diamond"),
                    Card("Eight", "Club"),
                    Card("Six", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Club"),
                    Card("Nine", "Club"),
                ],
            ),
            {"id": "0", "type": "pair", "value": 7},
        )
        self.assertEqual(
            game._determine_hand_value(
                "0",
                [
                    Card("Six", "Spade"),
                    Card("Three", "Diamond"),
                    Card("Eight", "Club"),
                    Card("Five", "Heart"),
                    Card("Ace", "Spade"),
                    Card("Ace", "Club"),
                    Card("Nine", "Club"),
                ],
            ),
            {"id": "0", "type": "high", "value": 5},
        )

    def test_get_flush_pool(self):
        game = Game()
        c1 = Card("Ten", "Spade")
        c2 = Card("Five", "Heart")
        c3 = Card("Eight", "Diamond")
        c4 = Card("Two", "Spade")
        c5 = Card("Ace", "Spade")
        c6 = Card("Six", "Spade")
        c7 = Card("Nine", "Spade")
        self.assertEqual(
            game._get_flush_pool(
                [c1, c2, c3, c4, c5, c6, c7],
            ),
            [c1, c4, c5, c6, c7],
        )
        c1 = Card("Ten", "Heart")
        c2 = Card("Five", "Spade")
        c3 = Card("Eight", "Diamond")
        c4 = Card("Two", "Spade")
        c5 = Card("Ace", "Spade")
        c6 = Card("Six", "Heart")
        c7 = Card("Nine", "Spade")
        self.assertEqual(
            game._get_flush_pool(
                [c1, c2, c3, c4, c5, c6, c7],
            ),
            [],
        )

    def test_calculate_straight_value(self):
        game = Game()
        self.assertEqual(
            game._calculate_straight_value(
                [
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Six", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ],
            ),
            25,
        )
        self.assertEqual(
            game._calculate_straight_value(
                [
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Spade"),
                    Card("Two", "Heart"),
                    Card("Six", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ],
            ),
            0,
        )

    def test_calculate_value(self):
        game = Game()
        self.assertEqual(
            game._calculate_value(
                [
                    Card("Two", "Spade"),
                    Card("Three", "Spade"),
                    Card("Four", "Spade"),
                    Card("Five", "Spade"),
                    Card("Six", "Spade"),
                    Card("Seven", "Spade"),
                    Card("Eight", "Spade"),
                ],
            ),
            28,
        )
