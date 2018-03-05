from typing import Any

class Tree:
    pass


def levelorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit every node in Tree t in level order and act on the node
    as you visit it.
    >>> t = descendants_from_list(Tree(0),
                                  [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit(t, act)
    """
    to_act = Queue()
    to_act.add(t)
    while not to_act.is_empty():
        tree = to_act.remove()
        act(tree)
        for child in tree.children:
            to_act.add(child)


def visit_level(t: Tree, act: Callable[[Tree], Any], n: int) -> int:
    """
    """
    if n == 1:
        act(t)
        return 1
    else:
        return sum([
            visit_level(child, act, n - 1)
            for child in t.children])


if __name__ == "__main__":
    import doctest
    doctest.testmod