from Deck import Deck
from Player import Player


class Game:
    def __init__(self, num_players=10):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        for p in range(0, num_players):
            self.players.append(Player(p))
        self.house = []
        self.outcome = []

    def deal(self):
        for p in self.players:
            p.add_card(self.deck.deal())
        for p in self.players:
            p.add_card(self.deck.deal())
        for i in range(0, 5):
            self.house.append(self.deck.deal())

    def get_house(self):
        r = "House: "
        for c in self.house:
            r += str(c) + ", "
        return r[:-2]

    def get_player(self, id):
        return self.players[id]

    def find_outcome(self, hand):
        pool = hand + self.house
        return self.outcome

    # Hand value highest to lowest
    # 1. Royal Flush
    # 2. Straight Flush
    # 3. Four of a Kind
    # 4. Full House
    # 5. Flush
    # 6. Straight
    # 7. Three of a Kind
    # 8. Two Pair
    # 9. Pair
    # 10. High Card
    def _is_royal_flush(self, pool):
        if not self._is_flush(pool):
            return False
        value = 0
        for c in pool:
            value += c.get_value()
        if value == 55:
            return True
        else:
            return False

    def _is_straight_flush(self, pool):
        if self._is_straight(pool) and self._is_flush(pool):
            return True
        return False

    def _is_flush(self, pool):
        suit = ""
        for c in pool:
            if suit == "":
                suit = c.get_suit()
            elif c.get_suit() != suit:
                return False
        return True

    def _is_straight(self, pool):
        r = []
        for c in pool:
            r.append(c.get_value())
        r = sorted(r)
        low = None
        for i, c in enumerate(r):
            if i == 0:
                low = c
            elif low + i != c:
                return False
        return True

    def _is_four_of_kind(self, pool):
        if (
            self._find_duplicates(pool[0].get_value(), pool) == 4
            or self._find_duplicates(pool[1].get_value(), pool) == 4
        ):
            return True
        else:
            return False

    def _is_full_house(self, pool):
        print(
            self._find_duplicates(pool[0].get_value(), pool),
            self._find_duplicates(pool[1].get_value(), pool),
        )
        if (
            self._find_duplicates(pool[0].get_value(), pool) == 3
            and self._find_duplicates(pool[1].get_value(), pool) == 2
        ) or (
            self._find_duplicates(pool[0].get_value(), pool) == 2
            and self._find_duplicates(pool[1].get_value(), pool) == 3
        ):
            return True
        else:
            return False

    def _is_three_of_kind(self, pool):
        if (
            self._find_duplicates(pool[0].get_value(), pool) == 3
            or self._find_duplicates(pool[1].get_value(), pool) == 3
        ):
            return True
        else:
            return False

    def _is_two_pair(self, pool):
        if (
            self._find_duplicates(pool[0].get_value(), pool) == 2
            and self._find_duplicates(pool[1].get_value(), pool) == 2
        ):
            return True
        else:
            return False

    def _is_pair(self, pool):
        if (
            self._find_duplicates(pool[0].get_value(), pool) == 2
            or self._find_duplicates(pool[1].get_value(), pool) == 2
        ):
            return True
        else:
            return False

    def _find_duplicates(self, v, pool):
        n = 0
        for c in pool:
            if v == c.get_value():
                n += 1
        return n

    def _get_highest_card(self, pool):
        return max(pool[0].get_value(), pool[1].get_value())
