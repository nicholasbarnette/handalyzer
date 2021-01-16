from Deck import Deck
from Player import Player


class Game:
    def __init__(self, players=[], num_players=9, house=[]):
        self.players = []
        excluded_cards = house[0:5]
        if len(players) > 0:
            for p in players:
                self.players.append(p)
                for c in p.get_hand():
                    excluded_cards.append(c)
        for p in range(len(players), num_players):
            self.players.append(Player(id=p))
        self.deck = Deck(exclude=excluded_cards)
        self.deck.shuffle()
        self.house = house[0:5]
        self.outcome = []

    def deal(self):
        for i, p in enumerate(self.players):
            if len(p.get_hand()) == 0:
                p.add_card(self.deck.deal())
        for i, p in enumerate(self.players):
            if len(p.get_hand()) == 1:
                p.add_card(self.deck.deal())

    def deal_flop(self):
        if len(self.house) < 3:
            for i in range(0, 3 - len(self.house)):
                self.house.append(self.deck.deal())

    def deal_turn(self):
        if len(self.house) < 4:
            for i in range(0, 4 - len(self.house)):
                self.house.append(self.deck.deal())

    def deal_river(self):
        if len(self.house) < 5:
            for i in range(0, 5 - len(self.house)):
                self.house.append(self.deck.deal())

    def get_house(self):
        return self.house

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
            t = self._determine_hand_value(p.get_id(), pool)
            hand_outcomes[t["type"]] = self._insert_ordered(
                hand_outcomes[t["type"]],
                t,
            )
        out = []
        for k in hand_outcomes.keys():
            out = out + hand_outcomes[k]
        return out

    def _determine_hand_value(self, id, pool):
        if self._is_royal_flush(pool):
            return {"id": id, "type": "royal_flush", "value": 55, "decider": []}
        elif self._is_straight_flush(pool):
            return {
                "id": id,
                "type": "straight_flush",
                "value": self._calculate_straight_value(self._get_flush_pool(pool)),
                "decider": self._get_tie_breaker(
                    self._get_flush_pool(pool),
                    [],
                    5,
                ),
            }
        elif self._is_four_of_kind(pool):
            return {
                "id": id,
                "type": "four_kind",
                "value": pool[0].get_value()
                if self._find_duplicates(pool[0].get_value(), pool) == 4
                else pool[1].get_value(),
                "decider": self._get_tie_breaker(
                    pool,
                    [
                        pool[0].get_value()
                        if self._find_duplicates(pool[0].get_value(), pool) == 4
                        else pool[1].get_value()
                    ],
                    1,
                ),
            }
        elif self._is_full_house(pool):
            return {
                "id": id,
                "type": "full_house",
                "value": pool[0].get_value()
                if self._find_duplicates(pool[0].get_value(), pool) == 3
                else pool[1].get_value(),
                "decider": [
                    pool[0].get_value()
                    if self._find_duplicates(pool[0].get_value(), pool) == 3
                    else pool[1].get_value()
                ]
                * 3
                + [
                    pool[0].get_value()
                    if self._find_duplicates(pool[0].get_value(), pool) == 2
                    else pool[1].get_value()
                ]
                * 2,
            }
        elif self._is_flush(pool):
            return {
                "id": id,
                "type": "flush",
                "value": self._calculate_value(self._get_flush_pool(pool)),
                "decider": self._get_tie_breaker(
                    self._get_flush_pool(pool),
                    [],
                    5,
                ),
            }
        elif self._is_straight(pool):
            return {
                "id": id,
                "type": "straight",
                "value": self._calculate_straight_value(pool),
                "decider": [],
            }
        elif self._is_three_of_kind(pool):
            return {
                "id": id,
                "type": "three_kind",
                "value": pool[0].get_value()
                if self._find_duplicates(pool[0].get_value(), pool) == 3
                else pool[1].get_value(),
                "decider": self._get_tie_breaker(
                    pool,
                    [
                        pool[0].get_value()
                        if self._find_duplicates(pool[0].get_value(), pool) == 3
                        else pool[1].get_value()
                    ],
                    2,
                ),
            }
        elif self._is_two_pair(pool):
            return {
                "id": id,
                "type": "two_pair",
                "value": pool[0].get_value()
                if pool[0].get_value() > pool[1].get_value()
                else pool[1].get_value(),
                "decider": self._get_tie_breaker(
                    pool, [pool[0].get_value(), pool[1].get_value()], 1
                ),
            }
        elif self._is_pair(pool):
            return {
                "id": id,
                "type": "pair",
                "value": pool[0].get_value()
                if self._find_duplicates(pool[0].get_value(), pool) == 2
                else pool[1].get_value(),
                "decider": self._get_tie_breaker(
                    pool,
                    [
                        pool[0].get_value()
                        if self._find_duplicates(pool[0].get_value(), pool) == 2
                        else pool[1].get_value()
                    ],
                    3,
                ),
            }
        else:
            h = pool[0] if pool[0].get_value() > pool[1].get_value() else pool[1]
            return {
                "id": id,
                "type": "high",
                "value": h.get_value(),
                "decider": self._get_tie_breaker(pool, [h.get_value()], 4),
            }

    def _get_tie_breaker(self, pool, match, n_kickers):
        p = pool.copy()
        tb = []
        i = len(pool) - 1
        while i >= 0:
            c = pool[i]
            if c.get_value() in match:
                tb.append(c.get_value())
                del p[i]
            i -= 1
        tb = sorted(tb, reverse=True)
        cc = sorted(p, key=lambda c: c.get_value(), reverse=True)
        for c in cc:
            if len(tb) < 5:
                tb.append(c.get_value())
        return tb

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
                if o["value"] >= p["value"] and self._find_winner(
                    o["decider"], p["decider"]
                ):
                    na.insert(i, o)
                    break
                elif i == len(na) - 1:
                    na.append(o)
                    break
        return na

    def _find_winner(self, a, b):
        for i in range(len(a)):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
        return False

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
