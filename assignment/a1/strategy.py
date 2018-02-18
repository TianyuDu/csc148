"""
revision 3
This file contains all essential files for strategy
"""
import random
# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: "Game") -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

# TODO: Implement a random strategy.


def random_strategy(game: "Game") -> str:
    """
    Take game as the input through random selection,
    Randomly choose one of the curret possible
    move of given game, and return it as a str.

    This method includes randomness, so no example will be provided.
    """
    possible_moves = game.current_state.get_possible_moves()  # List
    choice_idx = random.randrange(len(possible_moves))
    return possible_moves[choice_idx]


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
