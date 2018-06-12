"""
limits of recursion
"""
from node import LinkedListNode
from subtract_square_game import SubtractSquareGame
from subtract_square_state import SubtractSquareState


def recursive_append(b: LinkedListNode, data: object) -> None:
    """" recursively append a node with data to linked list headed by b"""
    if b.next_ is None:
        b.next_ = LinkedListNode(data)
    else:
        recursive_append(b.next_, data)


def fib(n: int) -> int:
    """ Return nth fibonacci number

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(3)
    2
    """
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib_mem(n: int, seen: dict) -> int:
    """
    return nth fibonacci number *quickly*
    """
    if n not in seen:
        if n < 2:
            seen[n] = n
        else:
            seen[n] = fib_mem(n - 2, seen) + fib_mem(n - 1, seen)
    return seen[n]


def count_states(s1: SubtractSquareState) -> int:
    """ Return the number of game states reachable from here.
    """
    moves = s1.get_possible_moves()
    states = [s1.make_move(m) for m in moves]
    return 1 + sum([count_states(x) for x in states])


def count_states_mem(s1: SubtractSquareState, seen: dict) -> int:
    """
    Return the number of game states reachable from here *quickly*.
    """
    moves = s1.get_possible_moves()
    states = [s1.make_move(m) for m in moves]
    if s1.__repr__() not in seen:
        seen[s1.__repr__()] = 1 + sum([count_states_mem(x, seen) for x in states])
    return seen[s1.__repr__()]


if __name__ == "__main__":
    g = SubtractSquareGame(True)
    s = g.current_state
    # comment out the non-memoized after 36 or 49...
    print(count_states(s))
    print(count_states_mem(s, {}))
