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
        -1 * get_state_score(game, game.current_state.make_move(move))
        #  get_state_score() provides the STATE SCORE for the OPPO player
        #  in each resultent state.
        #  -1 * ... to calculate the STATE SCORE for player taking action now.
        for move in candidate
    ]
    max_index = canditate_prop.index(max(canditate_prop))
    return candidate[max_index]


def get_state_score(game, state):
    """
    Helper function
    """
    if game.is_over(state):  # Base case, leaf case.
        if game.is_winner(state.get_current_player_name()):
            return 1  # Current player wins, the STATE SCORE for
        # current player is 1.
        else:
            return -1  # Oppo player wins, the STATE SCORE for
        # current player is -1
    else:
        return max([
            -1 * get_state_score(game, state.make_move(move))
            # -1 * ... reflects the the MOVE SCORE for certain move
            # for current player
            for move in state.get_possible_moves()
        ])  # the max of MOVE SCORE becomes the STATE SCORE for current state
        #  for current player.


def iterative_minimax(game: Game) -> Any:
    """
    Doc String Omitted.
    """
    state = game.current_state
    candidate_moves = state.get_possible_moves()
    current_player = state.get_current_player_name()
    trees = [
        TreeNode(state.make_move(move))
        for move in candidate_moves
    ]  # Create tree nodes for candidate moves.
    for root in trees:
        # stack = [
        #     TreeNode(root.state.make_move(move))
        #     for move in root.state.get_possible_moves()
        # ]
        #
        # if game.is_over(root.state):
        #     game.current_state = root.state
        #     if game.is_winner(current_player):
        #         root.score = 1
        #     else:
        #         root.score = -1
        #     continue
        # for sub in stack:
        #     root.add_child(sub)
        stack = [root]  # Create current stack.
        while stack != []:
            exam_node = stack.pop()  # Take out the last node.
            if game.is_over(exam_node.state):
                game.current_state = exam_node.state
                if game.is_winner(current_player):
                    exam_node.score = 1
                else:
                    exam_node.score = -1
            else:
                if exam_node.children == []:
                    possible_moves = exam_node.state.get_possible_moves()
                    for m in possible_moves:
                        c_node = TreeNode(exam_node.state.make_move(m))
                        exam_node.add_child(c_node)
                    stack.append(exam_node)
                    for child in exam_node.children:
                        stack.append(child)
                else:
                    exam_node.score = exam_node.get_high_score()
    scores = [root.score for root in trees]
    max_idx = scores.index(max(scores))
    return candidate_moves[max_idx]


class TreeNode():
    def __init__(self, state: GameState):
        self.state = state
        self.children = []
        self.score = -99

    def add_child(self, c: "TreeNode"):
        self.children.append(c)

    def get_high_score(self):
        try:
            return max([
                child.score
                for child in self.children
            ])
        except ValueError:
            pass

if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
