from Game import Game
from Player import Player
from Card import Card


g = Game()
g.deal()

print(g.get_house())
for p in range(len(g.players)):
    print(g.get_player(p))
print(g.find_outcome())


print()
p1 = Player(
    id=0, hand=[Card(rank="King", suit="Diamond"), Card(rank="Queen", suit="Spade")]
)
g = Game(player=p1)
g.deal()
print(g.get_house())
for p in range(len(g.players)):
    print(g.get_player(p))
print(g.find_outcome())