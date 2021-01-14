class Player:
    def __init__(self, id, hand=[]):
        self.id = id
        self.hand = hand[0:2]

    def add_card(self, card):
        if len(self.hand) < 2:
            self.hand.append(card)
            return True
        return False

    def get_hand(self):
        return self.hand

    def get_id(self):
        return self.id

    def __str__(self):
        s = "Player %d: " % (self.id)
        if len(self.hand) == 0:
            s += "Empty"
            return s
        else:
            for c in self.hand:
                s += str(c) + ", "
            return s[:-2]
