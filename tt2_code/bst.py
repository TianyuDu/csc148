"""
BTNode and BST classes
"""
from typing import Union, Any


class BTNode:
    """Binary Tree node."""

    def __init__(self, data: object,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        """
        Create BTNode (self) with data and children left and right.
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

    def __repr__(self):
        """ (BTNode) -> str

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

    def __contains__(self, data):
        """ (BTNode, object) -> value

        Return whether tree rooted at node contains value.

        >>> BTNode.__contains__(None, 5)
        False
        >>> t = BTNode(5, BTNode(7), BTNode(9))
        >>> t.__contains__(7)
        True
        >>> 9 in t
        True
        >>> 11 in t
        False
        """
        if self is None:
            return False
        else:
            return (self.data == data
                    # call with BTNode in case self.left, self.right are None
                    or BTNode.__contains__(self.left, data)
                    or BTNode.__contains__(self.right, data))


class BST:
    """
    Manages a binary search tree, even when the root is None or changes.

    root - root of binary search tree

    Assumptions:
        -- all data in root.left is less than root.data
        -- all data in root.right is more than root.data
        -- None indicates an empty tree
    """

    def __init__(self, root: BTNode=None) -> None:
        """
        Create BST with BTNode root.
        """
        self.root = root

    def __repr__(self):
        """ (BST) -> str

        Represent BST (self) as a string that can be evaluated
        to an equivalent BST.

        >>> b = BST(BTNode(5))
        >>> b
        BST(BTNode(5, None, None))
        """
        return 'BST({})'.format(repr(self.root))

    def __str__(self):
        """ (BST) -> str

        Return a user-friendly string representation of BST (self).

        >>> b = BST(BTNode(5, BTNode(4), BTNode(6)))
        >>> print(b)
            6
        5
            4
        <BLANKLINE>
        """
        # use BTNode.__str__
        return str(self.root)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
