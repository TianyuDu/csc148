"""
Revision: Final 2
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, List
from game import Game
from game_state import GameState


def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Game) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: Game) -> Any:
    """
    Recursive version of Minimax strategy. This is a wrapper of the recursion
    core of this strategy. Since initializing method of game requires input
    function so no example will be provided to this function.
    """
    candidate = game.current_state.get_possible_moves()
    canditate_prop = [
        -1 * get_state_score(game, game.current_state.make_move(
            move
        ))
        #  get_state_score() provides the STATE SCORE for the OPPO player
        #  in each resultent state.
        #  -1 * ... to calculate the STATE SCORE for player taking action now.
        for move in candidate
    ]
    max_index = canditate_prop.index(max(canditate_prop))
    assert len(canditate_prop) == len(candidate), "Inconsistent length."
    return candidate[max_index]


def get_state_score(game, state):
    """
    This is the helper function for the recursive version of min max strategy,
    this is the recursion part of that strategy. To initialize game, we need
    input method so no example is proveded.
    """
    # if game.is_over(state):  # Base case, leaf case.
    if state.get_possible_moves() == []:
        # current_player = state.get_current_player_name()
        # if current_player == "p1":
        #     other_player = "p2"
        # else:
        #     other_player = "p1 "
        game.current_state = state
        current_player = state.get_current_player_name()
        if current_player == "p1":
            other_player = "p2"
        else:
            other_player = "p1"
        if game.is_winner(current_player):
            return 1  # Current player wins, the STATE SCORE for
        elif game.is_winner(other_player):
            return -1
        return 0
        # current player is -1
    else:
        return max([
            -1 * get_state_score(game, state.make_move(move))
            # -1 * ... reflects the the MOVE SCORE for certain move
            # for current player
            for move in state.get_possible_moves()
        ])  # the max of MOVE SCORE becomes the STATE SCORE for current state
        #  for current player.


def iterative_minimax_strategy(game: Game) -> Any:
    """
    The iterative version of mini max strategy.
    It will create a tree stracture to record score of every possible branching
    of game state from current state and return the best possible state.
    """
    state = game.current_state
    candidate_moves = game.current_state.get_possible_moves()
    root = TreeNode(state=state)
    stack = [root]
    while stack != []:
        exam_node = stack.pop()
        if game.is_over(exam_node.state):
            # exam_node.score = -1
            game.current_state = exam_node.state
            current_player = exam_node.state.get_current_player_name()
            if current_player == "p1":
                other_player = "p2"
            else:
                other_player = "p1"
            if game.is_winner(current_player):  # If win.
                exam_node.score = 1
            elif game.is_winner(other_player):  # If loss (opponent wins)
                exam_node.score = -1
            else:  # Else, considered as tie.
                exam_node.score = 0
            # elif game.is_winner(other_player):
            #     exam_node.score = -1
            # else:
            #     exam_node.score = 0
        elif exam_node.children == []:
            possible_moves = exam_node.state.get_possible_moves()
            stack.append(exam_node)
            for move in possible_moves:
                child_node = TreeNode(
                    state=exam_node.state.make_move(move))
                exam_node.add_child(child_node)
                stack.append(child_node)
        else:
            scores = [- c.score for c in exam_node.children]
            exam_node.score = max(scores)
    # Root object now has all information it needs.
    scores = [- c.score for c in root.children]
    max_idx = scores.index(max(scores))
    return candidate_moves[max_idx]


class TreeNode:
    """
    TreeNode class used to implement the iterative version of minimax strategy.
    state: A GameState object that
    """
    state: GameState
    children: List["TreeNode"]

    def __init__(self, state=None):
        """
        Initializing methods for TreeNode object.
        >>> t = TreeNode()
        >>> t.score = 3
        >>> t.score
        3
        """
        self.state = state
        self.children = list()
        self.score = None

    def add_child(self, c: "TreeNode"):
        """
        Helper function, adding a new TreeNode to this TreeNode's children list.
        a  = TreeNode
        >>> t = TreeNode()
        >>> t2 = TreeNode()
        >>> t.add_child(t2)
        >>> t2 in t.children
        True
        """
        self.children.append(c)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod(verbose=False)
