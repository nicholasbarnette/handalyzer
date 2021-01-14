from Game import Game
from Player import Player
from Card import Card


c1 = Card(rank="Ace", suit="Diamond")
c2 = Card(rank="Ace", suit="Spade")
PLAYER = Player(id=0, hand=[c1, c2])
HANDS = 10000


def run_hands():
    wins = 0
    for i in range(HANDS):
        g = Game(player=PLAYER)
        g.deal()
        if g.find_outcome()[0]["id"] == 0:
            wins += 1
    print(
        "Win Percent [%s %s]: %d"
        % (str(c1), str(c2), round(wins / HANDS * 10000) / 100)
        + "%"
    )


run_hands()