"""# from queue_as_list import Queue
"""
from csc148_queue import Queue
from typing import List


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    def __init__(self, value: object=None, children: List['Tree']=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        self.children = children.copy() if children else []


def leaf_count(t: Tree) -> int:
    """
    Return the number of leaves in Tree t.
    >>> t = Tree(7)
    >>> leaf_count(t)
    1
    >>> t = descendants_from_list(Tree(7),[0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> leaf_count(t)
    6
    """
    if not t.children:
        return 1
    else:
        return sum([leaf_count(x) for x in t.children])


def height(t: Tree) -> int:
    """
    Return 1 + length of longest path of t.
    >>> t = Tree(13)
    >>> height(t)
    1
    >>> t = descendants_from_list(Tree(13),[0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> height(t)
    3
    """
    # 1 more edge than the maximum height of a child, except
    # what do we do if there are no children?
    # helpful helper function
    if not t.children:
        return 1
    else:
        return 1 + max([height(x) for x in t.children])
    # if t.children == []:
    #     return 1
    # else:
    #     return 1 + max([height(x) for x in t.children])


def arity(t: Tree) -> int:
    """
    Return the maximum branching factor (arity) of Tree t.
    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    if t.children == []:
        return 0
    else:
        return max([len(t.children)] + [arity(x) for x in t.children])
    # return max([len(t.children)] + [arity(x) for x in t.children])


def descendants_from_list(t, list_, arity):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int arity: maximum branching factor
    @rtype: Tree

    # >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    # Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, arity):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


if __name__ == '__main__':
    import doctest
    doctest.testmod()
