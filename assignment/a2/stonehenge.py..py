"""
File containing StonehengeState and StonehengeGame
"""
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    Game object of StonehengGame.
    """
    state: GameState

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        self.state = StonehengeState()

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        pass

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not this game is over at state.
        """
        pass

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        raise NotImplementedError

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """

class StonehengeState(GameState, side_length=3):
    """
    Game State containing information about currrent state of
    Stonehenge Game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        self.p1_turn = is_p1_turn

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        pass

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        pass

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: Any) -> 'GameState':
        """
        Return the GameState that results from applying move to this GameState.
        """
        pass

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        pass

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        pass
