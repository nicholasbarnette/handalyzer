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
                    Card("Ten", "Spade"),
                    Card("Jack", "Spade"),
                    Card("Queen", "Spade"),
                    Card("King", "Spade"),
                    Card("Ace", "Spade"),
                ]
            ),
            True,
        )
        self.assertEqual(
            self.game._is_royal_flush(
                [
                    Card("Ten", "Spade"),
                    Card("Jack", "Heart"),
                    Card("Queen", "Spade"),
                    Card("King", "Spade"),
                    Card("Ace", "Spade"),
                ]
            ),
            False,
        )
        self.assertEqual(
            self.game._is_royal_flush(
                [
                    Card("Two", "Spade"),
                    Card("Jack", "Spade"),
                    Card("Queen", "Spade"),
                    Card("King", "Spade"),
                    Card("Ace", "Spade"),
                ]
            ),
            False,
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
                    Card("Jack", "Spade"),
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
        self.assertSequenceEqual(
            self.game._find_outcome([], {"id": 0, "value": 55}),
            [{"id": 0, "value": 55}],
        )