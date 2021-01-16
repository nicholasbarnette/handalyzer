from Game import Game
from Player import Player
from Card import Card


PLAYERS = [
    Player(
        id=0, hand=[Card(rank="Ace", suit="Diamond"), Card(rank="Ace", suit="Spade")]
    ),
    Player(id=1, hand=[Card(rank="Ace", suit="Club"), Card(rank="Ace", suit="Heart")]),
    Player(
        id=2,
        hand=[Card(rank="Queen", suit="Diamond"), Card(rank="Jack", suit="Spade")],
    ),
]
HANDS = 10000
NUM_PLAYERS = 4


def run_hands():
    wins = {}
    for i in range(HANDS):
        g = Game(players=PLAYERS, num_players=NUM_PLAYERS)
        g.deal()
        outcome = g.find_outcome()

        if not outcome[0]["id"] in wins.keys():
            wins[outcome[0]["id"]] = 1
        else:
            wins[outcome[0]["id"]] += 1

    for p in wins.keys():
        if p >= len(PLAYERS):
            continue
        h = PLAYERS[p].get_hand()
        print(
            "Player %d Win Percent [%s %s]: %d"
            % (
                p,
                str(h[0]),
                str(h[1]),
                round(wins[p] / HANDS * 1000) / 10,
            )
            + "%"
        )


run_hands()