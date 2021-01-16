from Game import Game
from Player import Player
from Card import Card


COMMUNITY_CARDS = [
    # Card(rank="Ace", suit="Heart"),
    # Card(rank="Ace", suit="Club"),
    # Card(rank="Ten", suit="Club"),
]
PLAYERS = [
    Player(
        id=0, hand=[Card(rank="Ace", suit="Diamond"), Card(rank="Ace", suit="Spade")]
    ),
    Player(
        id=1, hand=[Card(rank="King", suit="Club"), Card(rank="King", suit="Heart")]
    ),
    Player(
        id=2,
        hand=[Card(rank="Queen", suit="Diamond"), Card(rank="Jack", suit="Spade")],
    ),
    Player(
        id=3,
        hand=[Card(rank="Queen", suit="Heart"), Card(rank="Two", suit="Spade")],
    ),
]
HANDS = 1000
NUM_PLAYERS = 4
INCLUDE_TIES = False


def print_results(wins):
    for p in sorted(wins.keys()):
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


def run_full_hands():
    wins = {}
    for i in range(HANDS):
        g = Game(players=PLAYERS, num_players=NUM_PLAYERS, house=COMMUNITY_CARDS)
        g.deal()
        g.deal_flop()
        g.deal_turn()
        g.deal_river()
        outcome = g.find_outcome()

        # print(g.get_house())
        # for o in outcome:
        #     print(o)

        decider_value = outcome[0]["value"]
        decider_sum = sum(outcome[0]["decider"])
        for i, v in enumerate(outcome):
            if decider_value == v["value"] and decider_sum == sum(v["decider"]):
                if not v["id"] in wins.keys():
                    wins[v["id"]] = 1
                else:
                    wins[v["id"]] += 1

                if not INCLUDE_TIES:
                    break

    print("Full hand")
    print_results(wins)


def run_partial_hands():
    wins = {"post_flop": {}, "post_turn": {}, "post_river": {}}

    for i in range(HANDS):
        g = Game(players=PLAYERS, num_players=NUM_PLAYERS, house=COMMUNITY_CARDS)
        g.deal()

        for t in wins.keys():
            if t == "post_flop":
                g.deal_flop()
            elif t == "post_turn":
                g.deal_turn()
            elif t == "post_river":
                g.deal_river()

            outcome = g.find_outcome()

            decider_value = outcome[0]["value"]
            decider_sum = sum(outcome[0]["decider"])
            for i, v in enumerate(outcome):
                if decider_value == v["value"] and decider_sum == sum(v["decider"]):
                    if not v["id"] in wins[t].keys():
                        wins[t][v["id"]] = 1
                    else:
                        wins[t][v["id"]] += 1

                    if not INCLUDE_TIES:
                        break

    for t in wins.keys():
        print("\n%s" % t)
        print_results(wins[t])


run_full_hands()
run_partial_hands()