"""
File containing StonehengeState and StonehengeGame
"""
from typing import List, Any
from game import Game
from game_state import GameState
from helper import illustrate_graph, create_graph, create_keys, get_ley_line_id


class StonehengeGame(Game):
    """
    Game object of StonehengGame.
    """
    current_state: "StonehengeState"
    instruction_string: str

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        side_length = int(input("Side length of board (1~5)"))
        self.current_state = StonehengeState(p1_starts, side_length)
        self.instruction_string = "missing instruction"

    def __str__(self) -> str:
        return ("This is a StonehengeGame with current state "
                + self.current_state.__str__())

    def get_instructions(self) -> str:
        """
        Return the instructions for this game
        """
        return self.instruction_string

    def count_node(self, state: "StonehengeState", check: str) -> int:
        """
        A helper function that help check the number of ley line occupied by
        give check string.
        """
        size = len(state.lls[0])  # number of ley line mark in each direction.
        return sum([
            int(state.lls[i][j] == check)
            for i in range(3)
            for j in range(size)
        ])

    def is_over(self, state: "StonehengeState") -> bool:
        """
        Return whether or not this game is over at state.
        """
        total_lls = len(state.lls[0]) * 3  # Total number of ley line.
        p1_count = self.count_node(state, "1")
        p2_count = self.count_node(state, "2")
        return (p1_count >= total_lls / 2
                or p2_count >= total_lls / 2)

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        if not self.is_over(self.current_state):
            return False  # If game not over yet, return False.
        total_lls = len(self.current_state.lls[0]) * 3
        check_point = player[-1]  # this would produce "1" for player "p1"
        # and "2"  for player "p2".
        return (self.count_node(self.current_state, check_point)
                >= (total_lls / 2))

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        Filter applied to the string to an upper case letter.
        """
        return string.upper()


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
        self.keys = create_keys(self.graph)

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        return illustrate_graph(self.graph, self.lls)

    def get_possible_moves(self) -> List[str]:
        """
        Return all possible moves that can be applied to this state.
        """
        total_ley_line = len(self.lls[0]) * 3
        p1_count = sum([
            int(item == "1")
            for sublist in self.lls
            for item in sublist
        ])
        p2_count = sum([
            int(item == "2")
            for sublist in self.lls
            for item in sublist
        ])
        if p1_count >= total_ley_line / 2 or p2_count >= total_ley_line / 2:
            # If the game is currently over, return empty possible move list.
            return []
        return [
            node
            for row in self.graph
            for node in row
            if (node not in ["1", "2"])
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
            not (self.get_current_player_name() == "p1"),
            # Flip the current player.
            self.side_length
        )
        assert (
            move.isupper()
            # and move in self.get_possible_moves()
        )
        new_state.graph = [g[:] for g in self.graph]
        new_state.lls = [l[:] for l in self.lls]
        ind = new_state.keys[move]
        current_player_flag = self.get_current_player_name()[-1]
        new_state.graph[ind[0]][ind[1]] = str(current_player_flag)
        # Update ley line state.
        for i in range(3):
            ley_line_id = get_ley_line_id(
                new_state.lls,
                i
            )  # Collection of leyline.
            # Current_lls_row state collection.
            for lls_number in range(len(ley_line_id)):
                current_line_ids = ley_line_id[lls_number]
                if new_state.lls[i][lls_number] == "@":
                    # ley line state for current focused line.
                    current_player_count = sum([
                        int(new_state.graph
                            [new_state.keys[value][0]]
                            [new_state.keys[value][1]]
                            == current_player_flag)
                        for value in current_line_ids
                    ])
                    if current_player_count >= len(current_line_ids) / 2:
                        new_state.lls[i][lls_number] = current_player_flag
        return new_state

    def is_valid_move(self, move: str) -> bool:
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


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
