SUITS = ["Spade", "Heart", "Club", "Diamond"]
RANKS = [
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]

SUIT_MAP = {
    "Spade": "S",
    "S": "Spade",
    "Heart": "H",
    "H": "Heart",
    "Club": "C",
    "C": "Club",
    "Diamond": "D",
    "D": "Diamond",
}
RANK_MAP = {
    "Two": "2",
    "2": "Two",
    "Three": "3",
    "3": "Three",
    "Four": "4",
    "4": "Four",
    "Five": "5",
    "5": "Five",
    "Six": "6",
    "6": "Six",
    "Seven": "7",
    "7": "Seven",
    "Eight": "8",
    "8": "Eight",
    "Nine": "9",
    "9": "Nine",
    "Ten": "10",
    "10": "Ten",
    "Jack": "J",
    "J": "Jack",
    "Queen": "Q",
    "Q": "Queen",
    "King": "K",
    "K": "King",
    "Ace": "A",
    "A": "Ace",
}


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        v = 0
        try:
            v = int(RANK_MAP[self.rank]) - 1
        except Exception as e:
            if self.rank == "Jack":
                v = 10
            elif self.rank == "Queen":
                v = 11
            elif self.rank == "King":
                v = 12
            elif self.rank == "Ace":
                v = 13
        finally:
            return v

    def __str__(self):
        return "%s%s" % (RANK_MAP[self.rank], SUIT_MAP[self.suit])
