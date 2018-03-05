"""
File containing StonehengeState and StonehengeGame
"""
from typing import List
from game import Game
from game_state import GameState
from helper import illustrate_graph, create_graph, create_keys, get_ley_line_id


class StonehengeGame(Game):
    """
    Game object of StonehengGame.
    """
    current_state: "StonehengeState"
    instruction_string: str

    def __init__(self, p1_starts: bool, side_length=None) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        Overridding the original initializing method in Game.
        Since initializing the stonehenge game object requires input function
        so no example will be provided.
        """
        if side_length is None:
            side_length = int(input("Side length of board (1~5)"))
        self.current_state = StonehengeState(p1_starts, side_length)
        self.instruction_string = """
        [What Stonehenge is about]
        Stonehenge is played on a hexagonal grid formed by removing the corners 
        from a triangular grid. 
        Boards can have various sizes based on their side-length 
        (the number of cells in the grid along the bottom), 
        but are always formed in a similar manner: 
        For side-length n, the first row has 2 cells, 
        and each row after has 1 additional cell up until
        there's a row with n + 1 cells, 
        after which the last row has only n cells in it.
        
        [How to win]
        Players take turns claiming cells (in the diagram: circles labelled 
        with a capital letter). When a player captures at least half of 
        the cells in a ley-line 
        then the player captures that ley-line. The rst player 
        to capture at least half of the ley-lines is the winner.
        A ley-line, once claimed, cannot be taken by the other player.        
        """

    def __str__(self) -> str:
        """
        Ths string method that return a string containing information about
        this game object, including it's type and it's current state. This
        overrids the original string method in Game.
        Since initializing the stonehenge game object requires input function
        so no example will be provided.
        """
        return ("This is a StonehengeGame with current state "
                + self.current_state.__str__())

    def __repr__(self) -> str:
        """
        The repr method returns a string containing information about
        this game object, including it's type and it's current state. This
        overrids the original string method in Game. This method overrids
        the original repr method in Game.
        Since initializing the stonehenge game object requires input function
        so no example will be provided.
        """
        return ("This is a StonehengeGame with current state "
                + self.current_state.__str__())

    def get_instructions(self) -> str:
        """
        Return the instructions for this game. This overrids the original
        get_instructions method in Game.
        
        >>> new_game = StonehengeGame(True, side_length=3)
        >>> new_game.get_instruction() == new_game.instruction_string
        True
        """
        return self.instruction_string

    def count_node(self, state: "StonehengeState", check: str) -> int:
        """
        A HELPER function that help check the number of ley line occupied by
        give check string.
        
        >>> new_game = StonehengeGame(True, side_length=3)
        >>> new_game.count_node(new_game.current_state, "p1")
        0
        >>> new_game.current_state.graph[0][0] = "2"
        >>> new_game.count_node(new_game.current_state, "p2")
        1
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

        >>> new_game = StonehengeGame(True, side_length=3)
        >>> new_game.is_over(new_game.current_state)
        False

        >>> new_game = StonehengeGame(True, side_length=3)
        >>> new_game.current_state.graph[0][0] = "1"
        >>> new_game.is_over(new_game.current_state)
        Falses
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

        >>> new_game = StonehengeGame(True, side_length=3)
        >>> new_game.is_winner("p1")
        False
        >>> new_game = StonehengeGame(True, side_length=3)
        >>> new_game.is_winner("p2")
        False
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

        >>> new_game = StonehengeGame(True, side_length=3)
        >>> new_game.str_to_move("a")
        A
		>>> new_game = StonehengeGame(True, side_length=3)
		>>> new_game.str_to_move("B")
		B
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

        >>> s = StonehengeState(True, 3)
        >>> s.p1_turn
        True
        >>> s.side_length
        3
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
        String methods could not pass the doctest based on string comparsion,
        so no example will be provided.
        """
        return illustrate_graph(self.graph, self.lls)

    def get_possible_moves(self) -> List[str]:
        """
        Return all possible moves that can be applied to this state.

        >>> s = StonehengeState(True, 2)
        >>> s.get_possible_moves()
        ['A', 'B', 'C']

        >>> s = StonehengeState(True, 3)
		>>> s.get_possible_moves()
		['A', 'B', 'C', 'D', 'E', 'F', 'G']
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

        >>> s = StonehengeState(True, 3)
        >>> s.get_current_player_name()
        'p1'
		>>> s = StonehengeState(False, 3)
		>>> s.get_current_player_name()
		'p2'
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: str) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        >>> s = StonehengeState(True, 2)
        >>> s.get_possible_moves()
        ['A', 'B', 'C']
        >>> s.make_move("A")
        >>> s.get_possible_moves()
        ['B', 'C']
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
                self.operations((i, lls_number, new_state,
                                 current_player_flag, current_line_ids))
        return new_state

    def operations(self, input_package):
        """
        The HELPER function for make move method to aviod too many nest and
        complicated codes, to improve the readability.
        No example will be provided for this helper funciton.
        """
        (i, lls_number, new_state,
         current_player_flag, current_line_ids) = input_package
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

    def is_valid_move(self, move: str) -> bool:
        """
        Return whether move is a valid move for this GameState. This method
        returns True is and only if a this passed in move is included in the
        possible move based on current state.

        >>> a = StonehengeState(True, 2)
        >>> a.get_possible_moves()
        ['A', 'B', 'C']
        >>> a.is_valid_move("C")
        True
        >>> a.is_valid_move("G")
        False
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        No example for the string and repr methods since it could not pass
        the string comparision based doctest.
        """
        return (
            "current player: {}\n".format(self.get_current_player_name()) +
            "current board:\n " +
            self.__str__()
        )

    def is_winner(self, player: str) -> bool:
        """
        This method examine if a player is winner, this method returns true
        if and only if this player passed in owned at least half of the total
        number of ley lines.
        Since initializing the stonehenge game object requires input function
        so no example will be provided.
        """
        total_lls = len(self.lls[0]) * 3
        check_point = player[-1]  # this would produce "1" for player "p1"
        # and "2"  for player "p2".
        return (self.count_ley_line(check_point)
                >= (total_lls / 2))

    def count_ley_line(self, check: str):
        """
        This method would count the total number of ley line that player passed
        in as input owns.
        Since initializing the stonehenge game object requires input function
        so no example will be provided.
        """
        size = len(self.lls[0])  # number of ley line mark in each direction.
        return sum([
            int(self.lls[i][j] == check)
            for i in range(3)
            for j in range(size)
        ])

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval[LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        Since initializing the stonehenge game object requires input function
        so no example will be provided.
        """
        possible_moves = self.get_possible_moves()
        current_player = self.get_current_player_name()
        if current_player == "p1":
            oppoosite_player = "p2"
        else:
            oppoosite_player = "p1"

        if self.is_winner(current_player):
            return 1.0
        elif self.is_winner(oppoosite_player):
            return -1.0

        total_moves = len(possible_moves)
        fail = 0
        for move in possible_moves:
            new_state = self.make_move(move)
            if new_state.is_winner(current_player):
                return 1.0  # Case1, at least one move leads to win.
            else:
                next_result = []
                for move2 in new_state.get_possible_moves():
                    new_state_2 = new_state.make_move(move2)
                    next_result.append(
                        new_state_2.is_winner(oppoosite_player)
                    )
                if all(next_result):  # If this move would lead to
                    #  a state that no matter what move the opposite player
                    #  make, opposite player wins, then this move is a
                    #  definitely failing move, which leads to definite
                    #  loss, and therefore should not be select. DEAD MOVE.
                    fail += 1  # Count the dead move.

        if fail == total_moves:
            return -1.0
        return fail / total_moves * - 2 + 1.0  # If no dead move, would return
        # 1.0, if all dead move, would return -1.0, linear estimation.


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod(verbose=True)
