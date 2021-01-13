class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def __str__(self):
        s = "Player %d: " % (self.id)
        if len(self.hand) == 0:
            s += "Empty"
            return s
        else:
            for c in self.hand:
                s += str(c) + ", "
            return s[:-2]
