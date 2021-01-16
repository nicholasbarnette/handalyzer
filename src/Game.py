from Deck import Deck
from Player import Player


class Game:
    def __init__(
        self,
        player=None,
        num_players=9,
    ):
        self.deck = Deck(exclude=player.get_hand() if player != None else [])
        self.deck.shuffle()
        self.players = []
        if player != None:
            self.players.append(player)
        for p in range(1, num_players):
            self.players.append(Player(id=p))
        self.house = []
        self.outcome = []

    def deal(self):
        for i, p in enumerate(self.players):
            if len(p.get_hand()) == 0:
                p.add_card(self.deck.deal())
        for i, p in enumerate(self.players):
            if len(p.get_hand()) == 1:
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

    def find_outcome(self):
        hand_outcomes = {
            "royal_flush": [],
            "straight_flush": [],
            "four_kind": [],
            "full_house": [],
            "flush": [],
            "straight": [],
            "three_kind": [],
            "two_pair": [],
            "pair": [],
            "high": [],
        }
        for p in self.players:
            pool = p.get_hand() + self.house

            if self._is_royal_flush(pool):
                hand_outcomes["royal_flush"].append(
                    {"id": p.get_id(), "type": "royal_flush", "value": 55}
                )
            elif self._is_straight_flush(pool):
                p_hand = self._calculate_straight_value(self._get_flush_pool(pool))
                hand_outcomes["straight_flush"] = self._insert_ordered(
                    hand_outcomes["straight_flush"],
                    {"id": p.get_id(), "type": "straight_flush", "value": p_hand},
                )
            elif self._is_four_of_kind(pool):
                if self._find_duplicates(pool[0].get_value(), pool) == 4:
                    hand_outcomes["four_kind"] = self._insert_ordered(
                        hand_outcomes["four_kind"],
                        {
                            "id": p.get_id(),
                            "type": "four_kind",
                            "value": pool[0].get_value(),
                        },
                    )
                else:
                    hand_outcomes["four_kind"] = self._insert_ordered(
                        hand_outcomes["four_kind"],
                        {
                            "id": p.get_id(),
                            "type": "four_kind",
                            "value": pool[1].get_value(),
                        },
                    )
            elif self._is_full_house(pool):
                if self._find_duplicates(pool[0].get_value(), pool) == 3:
                    hand_outcomes["full_house"] = self._insert_ordered(
                        hand_outcomes["full_house"],
                        {
                            "id": p.get_id(),
                            "type": "full_house",
                            "value": pool[0].get_value(),
                        },
                    )
                else:
                    hand_outcomes["full_house"] = self._insert_ordered(
                        hand_outcomes["full_house"],
                        {
                            "id": p.get_id(),
                            "type": "full_house",
                            "value": pool[1].get_value(),
                        },
                    )
            elif self._is_flush(pool):
                hand_outcomes["flush"].append(
                    {"id": p.get_id(), "type": "flush", "value": 55}
                )
            elif self._is_straight(pool):
                p_hand = self._calculate_straight_value(pool)
                hand_outcomes["straight"] = self._insert_ordered(
                    hand_outcomes["straight"],
                    {"id": p.get_id(), "type": "straight", "value": p_hand},
                )
            elif self._is_three_of_kind(pool):
                if self._find_duplicates(pool[0].get_value(), pool) == 3:
                    hand_outcomes["three_kind"] = self._insert_ordered(
                        hand_outcomes["three_kind"],
                        {
                            "id": p.get_id(),
                            "type": "three_kind",
                            "value": pool[0].get_value(),
                        },
                    )
                else:
                    hand_outcomes["three_kind"] = self._insert_ordered(
                        hand_outcomes["three_kind"],
                        {
                            "id": p.get_id(),
                            "type": "three_kind",
                            "value": pool[1].get_value(),
                        },
                    )
            elif self._is_two_pair(pool):
                if (
                    self._find_duplicates(pool[0].get_value(), pool) == 2
                    and self._find_duplicates(pool[1].get_value(), pool) == 2
                ):
                    hand_outcomes["two_pair"] = self._insert_ordered(
                        hand_outcomes["two_pair"],
                        {
                            "id": p.get_id(),
                            "type": "two_pair",
                            "value": pool[0].get_value()
                            if pool[0].get_value() > pool[1].get_value()
                            else pool[1].get_value(),
                        },
                    )
            elif self._is_pair(pool):
                hand_outcomes["pair"] = self._insert_ordered(
                    hand_outcomes["pair"],
                    {
                        "id": p.get_id(),
                        "type": "pair",
                        "value": pool[0].get_value() + pool[1].get_value(),
                    },
                )
            else:
                h = 0
                for c in p.get_hand():
                    h = max(h, c.get_value())
                hand_outcomes["high"] = self._insert_ordered(
                    hand_outcomes["high"],
                    {
                        "id": p.get_id(),
                        "type": "high",
                        "value": h,
                    },
                )

        out = []
        for k in hand_outcomes.keys():
            out = out + hand_outcomes[k]
        return out

    def _determine_hand_value(self, id, pool):
        if self._is_royal_flush(pool):
            return {"id": id, "type": "royal_flush", "value": 55}
        elif self._is_straight_flush(pool):
            return {
                "id": id,
                "type": "straight_flush",
                "value": self._calculate_straight_value(self._get_flush_pool(pool)),
            }
        elif self._is_four_of_kind(pool):
            return {
                "id": id,
                "type": "four_kind",
                "value": pool[0].get_value()
                if self._find_duplicates(pool[0].get_value(), pool) == 4
                else pool[1].get_value(),
            }
        elif self._is_full_house(pool):
            return {
                "id": id,
                "type": "full_house",
                "value": pool[0].get_value()
                if self._find_duplicates(pool[0].get_value(), pool) == 3
                else pool[1].get_value(),
            }
        elif self._is_flush(pool):
            return {
                "id": id,
                "type": "flush",
                "value": self._calculate_value(self._get_flush_pool(pool)),
            }
        elif self._is_straight(pool):
            return {
                "id": id,
                "type": "straight",
                "value": self._calculate_straight_value(pool),
            }
        elif self._is_three_of_kind(pool):
            return {
                "id": id,
                "type": "three_kind",
                "value": pool[0].get_value()
                if self._find_duplicates(pool[0].get_value(), pool) == 3
                else pool[1].get_value(),
            }
        elif self._is_two_pair(pool):
            return {
                "id": id,
                "type": "two_pair",
                "value": pool[0].get_value()
                if pool[0].get_value() > pool[1].get_value()
                else pool[1].get_value(),
            }
        elif self._is_pair(pool):
            return {
                "id": id,
                "type": "pair",
                "value": pool[0].get_value() + pool[1].get_value(),
            }
        else:
            h = 0
            for c in [pool[0], pool[1]]:
                h = max(h, c.get_value())
            return {
                "id": id,
                "type": "high",
                "value": h,
            }

    def _get_flush_pool(self, pool):
        cards = []
        suit = {}
        for c in pool:
            if c.get_suit() in suit.keys():
                suit[c.get_suit()] += 1
            else:
                suit[c.get_suit()] = 1
        check_suit = None
        for s in suit.keys():
            if suit[s] >= 5:
                check_suit = s
        for c in pool:
            if c.get_suit() == check_suit:
                cards.append(c)
        return cards

    def _calculate_straight_value(self, pool):
        r = []
        for c in pool:
            r.append(c.get_value())
        r = sorted(r, reverse=True)
        high = None
        n = 0
        hand_value = 0
        for i, v in enumerate(r):
            if i == 0 or high == None:
                high = v
                n = 1
                hand_value = v
            elif high - n == v:
                n += 1
                hand_value += v
            else:
                high = v
                n = 1
                hand_value = v
            if n >= 5:
                return hand_value
        return 0

    def _calculate_value(self, pool):
        v = 0
        for c in pool:
            v += c.get_value()
        return v

    def _insert_ordered(self, a, o):
        na = a
        if len(na) == 0:
            na.append(o)
        else:
            for i, p in enumerate(na):
                if o["value"] > p["value"]:
                    na.insert(i, o)
                    break
                elif i == len(na) - 1:
                    na.append(o)
                    break
        return na

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
        cards = {
            "Ace": False,
            "King": False,
            "Queen": False,
            "Jack": False,
            "Ten": False,
        }
        if not self._is_flush(pool):
            return False

        # Determine if player has one of the royal flush cards in their hand
        if not (
            pool[0].get_rank() in cards.keys() or pool[1].get_rank() in cards.keys()
        ):
            return False

        # Find the entire royal flush
        for c in pool:
            if c.get_rank() in cards.keys():
                cards[c.get_rank()] = True
        for c in cards.keys():
            if not cards[c]:
                return False
        return True

    def _is_straight_flush(self, pool):
        suit = {}
        for c in pool:
            if c.get_suit() in suit.keys():
                suit[c.get_suit()] += 1
            else:
                suit[c.get_suit()] = 1
        check_suit = None
        for s in suit.keys():
            if suit[s] >= 5:
                check_suit = s
        if not check_suit:
            return False
        r = []
        for c in pool:
            if c.get_suit() == check_suit:
                r.append(c.get_value())
        r = sorted(r, reverse=True)
        high = None
        n = 0
        for i, v in enumerate(r):
            if i == 0 or high == None:
                high = v
                n = 1
            elif high - n == v:
                n += 1
            else:
                high = v
                n = 1
            if n >= 5:
                return True
        return False

    def _is_flush(self, pool):
        suit = {}
        for c in pool:
            if c.get_suit() in suit.keys():
                suit[c.get_suit()] += 1
            else:
                suit[c.get_suit()] = 1
        for s in suit.keys():
            if suit[s] >= 5:
                return True
        return False

    def _is_straight(self, pool):
        r = []
        for c in pool:
            r.append(c.get_value())
        r = sorted(r, reverse=True)
        high = None
        n = 0
        for i, v in enumerate(r):
            if i == 0 or high == None:
                high = v
                n = 1
            elif high - n == v:
                n += 1
            else:
                high = v
                n = 1
            if n >= 5:
                return True
        return False

    def _is_four_of_kind(self, pool):
        if (
            self._find_duplicates(pool[0].get_value(), pool) == 4
            or self._find_duplicates(pool[1].get_value(), pool) == 4
        ):
            return True
        else:
            return False

    def _is_full_house(self, pool):
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
            and pool[0].get_value() != pool[1].get_value()
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
