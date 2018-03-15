"""
BTNode exercises
"""
from typing import Union, Any


class BTNode:
    """Binary Tree node.

    data - data this node represents
    left - left child
    right - right child
    """
    data: object
    left: Union["BTNode", None]
    right: Union["BTNode", None]

    def __init__(self, data: object,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        """
        Create BTNode (self) with data and children left and right.

        An empty BTNode is represented by None.

        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other: Any) -> bool:
        """
        Return whether BTNode (self) is equivalent to other.

        >>> BTNode(7).__eq__('seven')
        False
        >>> b1 = BTNode(7, BTNode(5))
        >>> b1.__eq__(BTNode(7, BTNode(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self) -> str:
        """
        Represent BTNode (self) as a string that can be evaluated to
        produce an equivalent BTNode.

        >>> BTNode(1, BTNode(2), BTNode(3))
        BTNode(1, BTNode(2, None, None), BTNode(3, None, None))
        """
        return 'BTNode({}, {}, {})'.format(self.data,
                                           repr(self.left),
                                           repr(self.right))

    def __str__(self, indent: str="") -> str:
        """
        Return a user-friendly string representing BTNode (self) inorder.
        Indent by indent.

        >>> b = BTNode(1, BTNode(2, BTNode(3)), BTNode(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = self.right.__str__(indent + '    ') if self.right else ''
        left_tree = self.left.__str__(indent + '    ') if self.left else ''
        return right_tree + '{}{}\n'.format(indent, str(self.data)) + left_tree


def list_longest_path(node: Union[BTNode, None]) -> list:
    """ List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    pass


def list_between(node: Union[BTNode, None], start: object, end: object) -> list:
    """
    Return a Python list of all data in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BTNode where all nodes in the subtree
    rooted at t.left are less than t.data, and all nodes in the subtree
    rooted at t.right are more than t.data

    Avoid visiting nodes with values less than start or greater than end.

    >>> b_left = BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    pass


def count_shallower(t: Union[BTNode, None], n: int) -> list:
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    >>> t = BTNode(0, BTNode(1, BTNode(2)), BTNode(3))
    >>> count_shallower(t, 2)
    3
    """
    pass


def concatenate_leaves(t: Union[BTNode, None]) -> str:
    """
    Return the string values in the Tree rooted at t concatenated from left to right.
    Assume all leaves have string value.

    >>> t1 = BTNode("one")
    >>> t2 = BTNode("two")
    >>> t3 = BTNode("three", t1, t2)
    >>> concatenate_leaves(t1)
    'one'
    >>> concatenate_leaves(t3)
    'onetwo'
    """
    pass


def count_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the number of leaves in BinaryTree t.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> count_leaves(None)
    0
    >>> count_leaves(t3)
    2
    """
    pass


def sum_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the leaves of BinaryTree t.  Return
    0 if t is empty.
    Assume all leaves have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_leaves(t2)
    2
    >>> sum_leaves(t3)
    3
    """
    pass


def sum_internal(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the internal nodes of BinaryTree t.  Return
    0 if t is empty.
    Assume all internal nodes have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_internal(t2)
    0
    >>> sum_internal(t3)
    3
    """
    pass


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()
