"""
Draft file.
"""

from helper import *
from game import Game
from game_state import GameState


def rec_find_max(game: Game, state: GameState):
    if game.is_over(state):
        if game.is_winner(state.get_current_player_name()):
            return 1
        else:
            return -1
    else:
        return max([
            - 1 * rec_find_max(game, state.make_move(move))
            for move in state.get_possible_moves()
        ])
