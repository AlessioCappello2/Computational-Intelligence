import random
from game import Game, Move, Player
from copy import deepcopy, copy
import math
from tqdm import tqdm
import numpy as np
from utils import max_sequence

class MinMaxPlayer(Player):
    def __init__(self, id: int, evaluation='simple') -> None:
        super().__init__()
        self.player_id = id
        self.evaluation = evaluation

    def evaluate(self, game: 'Game') -> int:
        res = game.check_winner()
        match self.evaluation:
            case 'simple':
                match self.player_id:
                    case 0: 
                        match res:
                            case 0: return 1
                            case 1: return -1
                            case -1: return 0
                    case 1: 
                        match res:
                            case 1: return 1
                            case 0: return -1
                            case -1: return 0
            case 'rcd':
                placeholders_player = np.where(game._board == self.player_id, 1, 0)
                placeholders_opponent = np.where(game._board == (self.player_id+1)%2, 1, 0)
                eval = 0
                match self.player_id:
                    case 0: 
                        match res:
                            case 0: eval+=1
                            case 1: eval-=1
                            case -1: eval=0
                    case 1: 
                        match res:
                            case 1: eval+=1
                            case 0: eval-=1
                            case -1: eval=0
                return eval + 0.8*max_sequence(placeholders_player) - 0.5*max_sequence(placeholders_opponent)
            

    def minimax(self, game: 'Game', depth, alfa, beta, isMaximizingPlaying):
        if game.check_winner() != -1 or depth == 0:
            return self.evaluate(game)
        
        if isMaximizingPlaying:
            max_eval = -math.inf
            available_moves = game.possible_moves(self.player_id)

            for m in available_moves:
                game_copy2 = deepcopy(game)
                fp, mv = m
                game_copy2.move(fp, mv, self.player_id)
                eval_score = self.minimax(game_copy2, depth - 1, alfa, beta, False)
                max_eval = max(max_eval, eval_score)
                alfa = max(alfa, eval_score)
                if beta <= alfa:
                    break
            return max_eval
        else:
            min_eval = math.inf
            available_moves = game.possible_moves((self.player_id+1)%2)

            for m in available_moves:
                game_copy2 = deepcopy(game)
                fp, mv = m
                game_copy2.move(fp, mv, (self.player_id+1)%2)
                eval_score = self.minimax(game_copy2, depth - 1, alfa, beta, True)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alfa:
                    break
            return min_eval


    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        best_score = -math.inf
        best_move = None

        available_moves = game.possible_moves(self.player_id)

        for m in tqdm(available_moves):
            game_copy2 = deepcopy(game)
            fp, mv = m
            game_copy2.move(fp, mv, self.player_id) #current_player_idx
            score = self.minimax(game_copy2, 3, -math.inf, math.inf, False)

            if score > best_score:
                best_score = score
                best_move = m
        
        from_pos, move = best_move
        return from_pos, move