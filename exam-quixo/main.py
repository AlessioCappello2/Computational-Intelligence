import random
from game import Game, Move, Player
from tqdm import tqdm
import os

from randomp import RandomPlayer
from minmax import MinMaxPlayer
from qlearning import QLPlayer
from weights_GA import MinMaxPlayerGA, find_genotype

class MyPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move
        

if __name__ == '__main__':

    # MinMax
    win = 0
    player1 = RandomPlayer()
    player2 = MinMaxPlayer(1, evaluation='rcd-enhanced', depth=3)
    for _ in range(10):
        g=Game()
        winner = g.play(player1, player2)
        print("The winner is ---> ", winner)
        if winner == 1: win +=1
    player1 = MinMaxPlayer(0, evaluation='rcd-enhanced', depth=3)
    player2 = RandomPlayer()
    for _ in range(10):
        g=Game()
        winner = g.play(player1, player2)
        print("The winner is --->", winner)
        if winner == 0: win +=1

    print("WINRATE:", win, "/20")
    
    # MinMax - GA
    # get the genotype (in the example I used one I found in a trial)
    # genotype = find_genotype()
    player1 = MinMaxPlayerGA(player_id=0, genotype=[5.774090728365553, 5.433056643709349, -6.127808991725557, -2.0758335834027912, 5.225734501084881, 1.6538618432485919, -0.008169021034825086])
    player2 = RandomPlayer()
    win = 0
    for _ in range(10):
        g=Game()
        winner = g.play(player1, player2)
        print("The winner is ---> ", winner)
        if winner == 0: win +=1
    player1 = RandomPlayer()
    player2 = MinMaxPlayerGA(player_id=1, genotype=[5.774090728365553, 5.433056643709349, -6.127808991725557, -2.0758335834027912, 5.225734501084881, 1.6538618432485919, -0.008169021034825086])
    for _ in range(10):
        g=Game()
        winner = g.play(player1, player2)
        print("The winner is --->", winner)
        if winner == 1: win +=1
    print("WINRATE:", win, "/20")
    
    # Q-Learning
    player1 = QLPlayer(0)
    player2 = RandomPlayer()
    qt = "q_table.txt"
    if os.path.exists(qt):
        player1.load_qtable(qt)
    else:
        player1.train_as0(300000)
    player1.set_epsilon(0)

    win = 0
    for _ in tqdm(range(2000)):
        g=Game()
        winner = g.play(player1, player2)
        if winner == 0: win += 1
    print("WINRATE:", win, "/2000")
    


