import random
from game import Game, Move, Player
from copy import deepcopy, copy
import math
from tqdm import tqdm
import numpy as np
from randomp import RandomPlayer
import struct
from utils import encode_move, decode_move
import sys

class QLPlayer(Player):
    def __init__(self, id: int, alfa=0.5, gamma=0.8, epsilon=1):
        super().__init__()
        self.player_id = id
        self.alfa = alfa
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = dict()

    
    def set_epsilon(self, epsilon):
        self.epsilon = epsilon

    
    def compact_string(self, matrix):
        matrix = matrix.flatten()
        compressed_data = struct.pack(f">{len(matrix)}b", *matrix)
        return compressed_data

    
    def get_q_value(self, state, action):
        if (state, action) not in self.q_table:
            self.q_table[(state, action)] = 0
        return self.q_table[(state, action)]
    

    def choice_action(self, state, actions):
        if np.random.uniform() < self.epsilon:
            return actions[np.random.choice(range(len(actions)))]
        else:
            state = self.compact_string(state)
            q_values = np.array([self.get_q_value(state, encode_move(action)) for action in actions])
            maximum = np.max(q_values)
            return actions[np.random.choice(np.where(q_values == maximum)[0])]
        
    
    def update(self, state, action, reward, next_state, next_actions):
        state = self.compact_string(state)
        next_state = self.compact_string(next_state)
        action = encode_move(action)
        q_value = self.get_q_value(state, action)
        next_q_values = np.array([self.get_q_value(next_state, encode_move(next_action)) for next_action in next_actions])
        maximum = np.max(next_q_values) if len(next_q_values) > 0 else 0
        self.q_table[(state, action)] = q_value + self.alfa * (reward + self.gamma * maximum - q_value)


    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        state = game.get_board()
        actions = game.possible_moves(self.player_id)
        from_pos, slide = self.choice_action(state, actions)
        return from_pos, slide
    

    def train_as0(self, episodes=50000):
        epsilon = np.linspace(1, 0.1, num=episodes, endpoint=True)
        players = [self, RandomPlayer()]

        for i in tqdm(range(episodes)):
            self.set_epsilon(epsilon[i])
            g = Game()
            winner = -1
            while winner < 0:
                g.current_player_idx += 1
                g.current_player_idx %= 2
                ok = False
                while not ok:
                    from_pos, slide = players[g.current_player_idx].make_move(
                        g)
                    state = g.get_board()
                    action = (from_pos, slide)
                    ok = g.move(from_pos, slide, g.current_player_idx)
                winner = g.check_winner()
                if winner != -1:
                    if g.current_player_idx == self.player_id:
                        next_state = g.get_board()
                        next_actions = g.possible_moves(self.player_id) 
                        reward = 1 if winner == self.player_id else -1
                        self.update(state, action, reward, next_state, next_actions)
                else:
                    g.current_player_idx += 1
                    g.current_player_idx %= 2
                    ok = False
                    reward = 0
                    while not ok:
                        from_pos, slide = players[g.current_player_idx].make_move(
                            g)
                        ok = g.move(from_pos, slide, g.current_player_idx)
                    winner = g.check_winner()
                    if winner != -1:
                        reward = 1 if winner == self.player_id else -1
                    next_state = g.get_board()
                    next_actions = g.possible_moves(self.player_id)
                    self.update(state, action, reward, next_state, next_actions)

            if i%(episodes-1)==0:
                with open(f"q_table.txt", "w") as f:
                    stout = sys.stdout
                    sys.stdout = f
                    for key, v in self.q_table.items():
                        print(key, v)
                    sys.stdout = stout


    def train_as1(self, episodes=50000):
        epsilon = np.linspace(1, 0.1, num=episodes, endpoint=True)
        players = [RandomPlayer(), self]

        for i in tqdm(range(episodes)):
            self.set_epsilon(epsilon[i])
            g = Game()
            winner = -1
            g.current_player_idx += 1
            g.current_player_idx %= 2
            from_pos, slide = players[g.current_player_idx].make_move(
                g)
            _ = g.move(from_pos, slide, g.current_player_idx)
            while winner < 0:
                g.current_player_idx += 1
                g.current_player_idx %= 2
                ok = False
                while not ok:
                    from_pos, slide = players[g.current_player_idx].make_move(
                        g)
                    state = g.get_board()
                    action = (from_pos, slide)
                    ok = g.move(from_pos, slide, g.current_player_idx)
                winner = g.check_winner()
                if winner != -1:
                    if g.current_player_idx == self.player_id:
                        next_state = g.get_board()
                        next_actions = g.possible_moves(self.player_id) 
                        reward = 1 if winner == self.player_id else -1
                        self.update(state, action, reward, next_state, next_actions)
                else:
                    g.current_player_idx += 1
                    g.current_player_idx %= 2
                    ok = False
                    reward = 0
                    while not ok:
                        from_pos, slide = players[g.current_player_idx].make_move(
                            g)
                        ok = g.move(from_pos, slide, g.current_player_idx)
                    winner = g.check_winner()
                    if winner != -1:
                        reward = 1 if winner == self.player_id else -1
                    next_state = g.get_board()
                    next_actions = g.possible_moves(self.player_id)
                    self.update(state, action, reward, next_state, next_actions)
            
            if i%(episodes-1)==0:
                with open(f"q_table.txt", "w") as f:
                    stout = sys.stdout
                    sys.stdout = f
                    for key, v in self.q_table.items():
                        print(key, v)
                    sys.stdout = stout

    
    def load_qtable(self, file):
        with open(file, "r") as f:
            for line in tqdm(f):
                line = line.strip()
                if line:
                    f = line.split(" ") 
                    state = f[0].lstrip("(").rstrip(",")
                    action = f[1].rstrip(")")
                    value = float(f[2])
                    self.q_table[(state, action)] = value