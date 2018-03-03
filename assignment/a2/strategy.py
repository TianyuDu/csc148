"""
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
    Doc
    """
    state = game.current_state
    candidate_moves = game.current_state.get_possible_moves()
    root = TreeNode(state=state)
    stack = [root]
    while stack != []:
        exam_node = stack.pop()
        if game.is_over(exam_node.state):
            exam_node.score = -1
        else:
            if exam_node.children == []:
                possible_moves = exam_node.state.get_possible_moves()
                stack.append(exam_node)
                for move in possible_moves:
                    child_node = TreeNode(
                        state=exam_node.state.make_move(move))
                    exam_node.add_child(child_node)
                    stack.append(child_node)
            else:
                # child_scores = exam_node.get_child_scores()
                # minus_scores = [-1 * s for s in child_scores]
                # # Calculate the highest minus score.
                # exam_node.score = max(minus_scores)
                exam_node.score = exam_node.get_max_neg_child_val()
    # scores = [root.get_min_score() for root in trees]
    # # scores = max([root.score for root in trees])
    # assert len(scores) == len(candidate_moves), "Inconsistent length."
    max_idx = root.get_max_neg_child_idx()
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

    def get_max_neg_child_val(self):
        scores = [- c.score for c in self.children]
        return max(scores)

    def get_max_neg_child_idx(self):
        # get the max negative score of children.
        scores = [- c.score for c in self.children]
        return scores.index(max(scores))

    def get_child_scores(self):
        return [c.score for c in self.children]

    def get_min_score(self):
        assert self.children != []
        return min([
            child.score
            for child in self.children
        ])


    def get_move_score(self):
        if self.children == []:
            assert self.score is not None
            return self.score
        if all([
            child_node.score == 1
            for child_node in self.children
        ]):
            return 1
        elif all([
            child_node.score == -1
            for child_node in self.children
        ]):
            return -1
        else:
            return 0

    def get_max_score(self):
        #  assert self.children != [], "This TreeNode is leaf and has no child."
        return max([-1] + [
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
