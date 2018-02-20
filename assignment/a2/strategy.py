"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from game import Game
from game_state import GameState

# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def recursive_minimax(game: Game):
    """
    Recursive version of Minimax strategy.
    """
    candidate = game.current_state.get_possible_moves()
    canditate_prop = [
        rec_find_max(game, game.current_state.make_move(move))
        for move in candidate
    ]
    max_index = canditate_prop.index(max(canditate_prop))
    return candidate[max_index]


def rec_find_max(game: Game, state: GameState):
    if game.is_over(state):  # Base case, leaf case.
        if game.is_winner(state.get_current_player_name()):
            return 1  # if current player is the winner, get point of 1.
        else:
            return -1  # if current player is the loser, get point of -1.
    else:
        return max([
            -1 * rec_find_max(game, state.make_move(move))
            for move in state.get_possible_moves()
        ])


def iterative_minimax(game: Game) -> Any:
    """
    Doc String Omitted.
    """
    pass

if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
