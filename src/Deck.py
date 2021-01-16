from Card import Card, SUITS, RANKS
from random import randint


class Deck:
    def __init__(self, exclude=[]):
        self.deck = self._generate_deck(exclude=exclude)
        self.length = len(self.deck)

    def _generate_deck(self, exclude):
        d = []
        for s in SUITS:
            for r in RANKS:
                add = True
                for c in exclude:
                    if c.get_rank() == r and c.get_suit() == s:
                        add = False
                        break
                if add:
                    d.append(Card(r, s))
        return d

    def shuffle(self):
        for i in range(0, 100):
            a = randint(0, self.length - 1)
            b = randint(0, self.length - 1)
            if a == b:
                b = a + 1
                if b > self.length - 1:
                    b = 0
            tmp_card = self.deck[a]
            self.deck[a] = self.deck[b]
            self.deck[b] = tmp_card
        return True

    def deal(self):
        self.length -= 1
        return self.deck.pop()

    def __len__(self):
        return self.length

    def __str__(self):
        s = "Deck: "
        for c in self.deck:
            s += str(c) + ", "
        return s[:-2]
