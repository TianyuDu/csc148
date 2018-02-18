"""
This is the main file for game interface and game interface
class if contained in this file.
Some other control flow codes are contained here.
"""
from typing import Any, Callable
from strategy import *
from game import *


class GameInterface:
    """
    A game interface for a two-player, sequential move, zero-sum,
    perfect-information game.

    game - the  game to be played
    p1_strategy - strategy for player 1
    p2_strategy - strategy for player 2
    """
    game: "Game"
    p1_strategy: Callable[[Any], Any]
    p2_strategy: Callable[[Any], Any]

    def __init__(self, game: "Game", p1_strategy: Callable[[Any], Any],
                 p2_strategy: Callable[[Any], Any]) -> None:
        """
        Initialize this GameInterface, setting its active game to game, and
        using the strategies p1_strategy for Player 1 and p2_strategy for
        Player 2.
        """
        first_player = input("Type y if player 1 is to make the first move: ")
        is_p1_turn = False
        if first_player.lower() == 'y':
            is_p1_turn = True

        self.game = game(is_p1_turn)
        self.p1_strategy = p1_strategy
        self.p2_strategy = p2_strategy

    def play(self) -> None:
        """
        Play the game.
        """
        current_state = self.game.current_state

        print(self.game.get_instructions())
        print(current_state)

        # Pick moves until the game is over
        while not self.game.is_over(current_state):
            move_to_make = None

            # Print out all of the valid moves
            possible_moves = current_state.get_possible_moves()
            print("The current available moves are:")
            for move in possible_moves:
                print(move)

            # Pick a (legal) move.
            while not current_state.is_valid_move(move_to_make):
                current_strategy = self.p2_strategy
                if current_state.get_current_player_name() == 'p1':
                    current_strategy = self.p1_strategy
                move_to_make = current_strategy(self.game)

            # Apply the move
            current_player_name = current_state.get_current_player_name()
            new_game_state = current_state.make_move(move_to_make)
            self.game.current_state = new_game_state
            current_state = self.game.current_state # Update current state.

            print("{} made the move {}. The game's state is now:".format(
                current_player_name, move_to_make))
            print(current_state)

        # Print out the winner of the game
        if self.game.is_winner("p1"):
            print("Player 1 is the winner!")
        elif self.game.is_winner("p2"):
            print("Player 2 is the winner!")
        else:
            print("It's a tie!")


# TODO: Replace None with the corresponding class name for your games.

# 's' should map to your implementation of Subtract Square, and 'c' should map
# to Chopsticks.
play = {'s': SubstractSquare,
                  'c': ChopSticks}

# The strategies you are to implement.  See strategy.py, and then decide
# how to modify this.
usable_strategies = {'r': random_strategy,
                     'i': interactive_strategy}

if __name__ == '__main__':
    games = ", ".join(["'{}': {}".format(key, PLAYABLE_GAMES[key].__name__) if
                       PLAYABLE_GAMES[key] is not None else
                       "'{}': None".format(key) for key in PLAYABLE_GAMES])

    strategies = ", ".join(["'{}': {}".format(key,
                                              usable_strategies[key].__name__)
                            if usable_strategies[key] is not None else
                            "'{}': None".format(key)
                            for key in usable_strategies])

    chosen_game = ''
    while chosen_game not in PLAYABLE_GAMES.keys():
        chosen_game = input(
            "Select the game you want to play ({}): ".format(games))

    p1 = ''
    p2 = ''

    while p1 not in usable_strategies.keys():
        p1 = input("Select the strategy for Player 1 ({}): ".format(strategies))

    while p2 not in usable_strategies.keys():
        p2 = input("Select the strategy for Player 2 ({}): ".format(strategies))

    GameInterface(PLAYABLE_GAMES[chosen_game], usable_strategies[p1],
                  usable_strategies[p2]).play()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
