"""
File containing StonehengeState and StonehengeGame
"""
from game import Game
from game_state import GameState
from typing import Dict, List, Any
from draft_2 import *


class StonehengeGame(Game):
    """
    Game object of StonehengGame.
    """
    current_state: GameState

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        side_length = int(input("Side length of board (1~5)"))
        self.current_state = StonehengeState(p1_starts, side_length)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        pass

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not this game is over at state.
        """
        size = len(state.lls[0])
        p1_count = sum([
            (state.lls[i][j] == "1")
            for i in range(3)
            for j in range(size)
        ])
        p2_count = sum([
            (state.lls[i][j] == "2")
            for i in range(3)
            for j in range(size)
        ])
        return (p1_count >= size / 2
                or p2_count >= size / 2)

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


class StonehengeState(GameState):
    """
    Game State containing information about currrent state of
    Stonehenge Game.
    """
    graph: List[List[int]]  # The graph representing the current board state.
    lls: List[List[str]]  # The ley line state.
    # Sublist 1: Horizontal
    # Sublist 2: From left-top to right-bottom
    # Sublist 3: From right-top to left-bottom

    def __init__(self, is_p1_turn: bool, side_length: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        self.p1_turn = is_p1_turn
        self.side_length = side_length
        assert 1 <= side_length <= 5
        self.graph = create_graph(n=side_length)
        self.lls = [
            ("@ " * (side_length + 1)).split()
            for _ in range(3)
        ]
        self.keys = dict()
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                self.keys[self.graph[i][j]] = (i, j)

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        return illustrate_graph(
            self.graph,
            self.lls
        )

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        return [
            node
            for row in self.graph
            for node in row
            if node != "1" and node != "2"
        ]

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: str) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        new_state = StonehengeState(
            not self.get_current_player_name() == "p1",
            self.side_length
        )
        assert (
            move.isupper()
            and move in self.get_possible_moves()
        )
        new_state.graph = self.graph[:]
        new_state.lls = self.lls[:]
        ind = new_state.keys[move]
        new_state.graph[ind[0]][ind[1]] = self.get_current_player_name()[-1]
        #  Check horizontal lines, line 1
        for i in range(len(new_state.graph)):
            row = new_state.graph[i]
            row_length = len(row)
            p1_total = sum([
                int(node == "1") for node in row
            ])
            p2_total = sum([
                int(node == "2") for node in row
            ])
            check_1, check_2 = False, False
            if p1_total >= row_length / 2:
                new_state.lls[0][i] = 1
                check_1 = True
            if p2_total >= row_length / 2:
                new_state.lls[0][i] = 2
                check_2 = True
            if check_1 and check_2:
                print("Warning!!! Make move conflict")
                raise Warning("Warning!!! Make move conflict")
        return new_state

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
        print(self.__str__())

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        pass


# if __name__ == "__main__":
# s = StonehengeGame(True)
# print(s.current_state)
