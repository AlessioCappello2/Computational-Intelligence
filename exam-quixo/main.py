import random
from game import Game, Move, Player

from copy import deepcopy, copy
from tqdm import tqdm
import sys

from randomp import RandomPlayer
from minmax import MinMaxPlayer

class MyPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move
        

if __name__ == '__main__':
    player1 = MyPlayer()
    player2 = RandomPlayer()
    #player2 = GA(population_size=50)
    #player2.train()
    #player2.currentSequence = 0
    #player2.currentIndex = 0

    '''
    win = 0
    for _ in range(20):
        g = Game()
        player2.currentIndex = 0
        player2.currentSequence = 0
        winner = g.play(player1, player2)
        print(f"Winner: Player {winner}")
        if winner == 1: win += 1
        g = Game()
        player2.currentIndex = 0
        player2.currentSequence = 0
        winner = g.play(player2, player1)
        if winner == 0: win += 0
        print(f"Winner: Player {winner}")

    print("WINRATE: ", win/40.0)
    '''
    player1 = RandomPlayer()
    player2 = MinMaxPlayer(1, evaluation='rcd')

    win = 0
    for _ in range(10):
        g=Game()
        winner = g.play(player1, player2)
        print("The winner is", winner)
        if winner == 1: win +=1
    print("WINRATE:", win, "/20")
