import random
from game import Game, Move, Player
from copy import deepcopy, copy
import math
from tqdm import tqdm

from randomp import RandomPlayer

class GA(Player):
    def __init__(self, population_size) -> None:
        super().__init__()
        self.population = [
            [((random.randint(0, 50)%5, random.randint(0, 4)), random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])) for _ in range(500)] for _ in range(population_size)
        ]
        self.fitnesses = [0.0 for _ in range(population_size)]
        self.currentSequence = 0
        self.currentIndex = 0


    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos, move = self.population[self.currentSequence][self.currentIndex]
        self.currentIndex += 1
        if self.currentIndex % 500 == 0:
            self.currentIndex = 0
            self.currentSequence += 1 # <<<
            if self.currentSequence == 5:
                self.currentSequence = 0
        return from_pos, move
    

    def tweak_individual(self, idx, parent, qty) -> None:
        toMutate = deepcopy(self.population[parent])
        for _ in range(qty):
            m = random.randint(0, 49)
            if random.random() < 0.33:
                toMutate[m] = ((random.randint(0, 50)%5, random.randint(0, 4)), random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])) 
            else:
                toMutate[m] = ((random.randint(0, 4), random.randint(0, 50)%5), toMutate[m][1])
        for i, x in enumerate(toMutate):
            self.population[idx][i] = x


    def evaluate_fitnesses(self, first: bool):
        fitnesses = []
        top = 5 if first is not True else 0
        for i in range(top, len(self.population)): #top, population_size
            win = 0
            for _ in range(50):
                g = Game()
                #player1 = self
                self.currentIndex = 0
                self.currentSequence = i
                player2 = RandomPlayer()
                winner = g.play(self, player2)
                if winner == 1: win+=1
            for _ in range(50): 
                g = Game()
                player1 = RandomPlayer()
                #player2 = self
                self.currentIndex = 0
                self.currentSequence = i
                winner = g.play(player1, self)
                if winner == 0: win+=1
            fitnesses.append(float (win)/100)
        for i, x in enumerate(fitnesses):
            self.fitnesses[top+i] = x 
    

    def train(self):
        first = True
        print("GA Training")
        for _ in tqdm(range(20)): # epochs
            top = 5 if first is not True else 0
            for idx in range(top, 30):
                self.tweak_individual(idx, random.randint(0, 4), random.randint(3, 10))
            self.evaluate_fitnesses(first)
            first = False
            couples = list(zip(self.population, self.fitnesses))
            couples = sorted(couples, key = lambda x: x[1], reverse=True)
            self.population, self.fitnesses = map(list, zip(*couples))