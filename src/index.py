from Game import Game


g = Game()
g.deal()

print(g.get_house())
for p in range(10):
    print(g.get_player(p))
