"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, List
from game import Game
from game_state import GameState

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Game) -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def recursive_minimax_strategy(game: Game) -> Any:
    """
    Recursive version of Minimax strategy.
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
    Helper function
    """
    if game.is_over(state):  # Base case, leaf case.
        if game.is_winner(state.get_current_player_name()):
            return 1  # Current player wins, the STATE SCORE for
        # current player is 1.
        return -1  # Oppo player wins, the STATE SCORE for
        # current player is -1
    else:
        return max([
            -1 * get_state_score(game, state.make_move(
                move
            ))
            # -1 * ... reflects the the MOVE SCORE for certain move
            # for current player
            for move in state.get_possible_moves()
        ])  # the max of MOVE SCORE becomes the STATE SCORE for current state
        #  for current player.


def iterative_minimax_strategy(game: Game) -> str:
    """
    Doc String Omitted.
    """
    state = game.current_state
    candidate_moves = game.current_state.get_possible_moves()
    our_player = game.current_state.get_current_player_name()
    if our_player == "p1":
        oppo_player = "p2"
    else:
        oppo_player = "p1"
    trees = [
        TreeNode(state.make_move(move))
        for move in candidate_moves
    ]  # Create tree nodes for candidate moves.
    #  So that we have tree roots for each canddiate move.
    for root in trees:  # We focus on the tree of each candidate move tryin to
        # calculate their score
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
            # If current node representing a game-over state.
            if game.is_over(exam_node.state):
                game.current_state = exam_node.state  # Assign state to game,
                # So that game could exam..
                if game.is_winner(our_player):
                    exam_node.score = 1  # OUR player is the winner.
                elif game.is_winner(oppo_player):
                    exam_node.score = -1  # if the OPPONENT player is the winner
            # Else, if the current representing a state that NOT over yet.
            else:
                if exam_node.children == []:
                    # If the current node has NOT been explored yet.
                    # Create a tree structure branching
                    # out all accessible states.
                    possible_moves = exam_node.state.get_possible_moves()
                    stack.append(exam_node)
                    for move in possible_moves:
                        child_node = TreeNode(
                            state=exam_node.state.make_move(move))
                        exam_node.add_child(child_node)
                        stack.append(child_node)
                        # Create TreeNode containing all accessible moves, and
                        # add them to the children of current TreeNode.

                    # stack.append(exam_node)
                    # # Add current PARENT back to stack.
                    # for child in exam_node.children:
                    #     stack.append(child)

                        # Add each children to the stack AFTER the parent node
                else:  # If the exam_node.children is non-empty, means we
                    # have explored this node bef ore and all of it's children
                    # should have been scored.
                    exam_node.score = exam_node.calculate_score()
    scores = [root.calculate_score() for root in trees]
    # scores = max([root.score for root in trees])
    assert len(scores) == len(candidate_moves), "Inconsistent length."
    max_idx = scores.index(max(scores))
    return candidate_moves[max_idx]


class TreeNode:
    """
    ..
    """
    state: GameState
    children: List["TreeNode"]

    def __init__(self, state=None):
        self.state = state
        self.children = list()
        self.score = None

    def add_child(self, c: "TreeNode"):
        self.children.append(c)

    def get_min_score(self):
        assert self.children != []
        return min([
            child.score
            for child in self.children
        ])

    def get_high_score(self):
        assert self.children != [], "This TreeNode is leaf and has no child."
        return max([
            child.score
            for child in self.children
        ])  # We don't have to concern the case
        # That the list comperhansion returns an empty list.

    def calculate_score(self):
        if self.children == []:
            assert self.score is not None
            return self.score
        if all([
                child_node.score == 1
                for child_node in self.children
        ]):
            return 2  # Order 1: if all possible give
        if all([
                child_node.score == -1
                for child_node in self.children
        ]):
            return -1
        if any([
                child_node.score == 1
                for child_node in self.children
        ]):
            return 1
        return 0


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
