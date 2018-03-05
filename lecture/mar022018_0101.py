"""
## Binary Trees
"""
from typing import Union

class BTNode:
    """
    A Binary Tree, i.e. arity 2.
    """
    def __init__(self, value,
                left: Union["BTNode", None]=None,
                right: Union["BTNode", None]=None) -> None:
        self.value, self.left, self.right = value, left, right
    
    def __repr__(self):
        """
        """
        pass


class BinaryTree:
    """
    """
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    
    def __contains__(self, value):
        """
        
        # >>> t = None
        # >>> 5 in t
        # False
        >>> t = BinaryTree(5, BinaryTree(7), BinaryTree(9))
        >>> 7 in t
        True
        """
        if self.left is None and self.right is None:
            return self.data == value
        elif self.left is None:
            return self.data == value or value in self.right
        elif self.right is None:
            return self.data == value or value in self.left
        else:
            return any([
                self.data == value,
                value in self.left,
                value in self.right
                ])


def contains(node, value):
    """
    
    >>> contains(None, 5)
    False
    >>> contains(BinaryTree(5, BinaryTree(7), BinaryTree(9)), 7)
    True
    """
    if node is None:
        return False
    else:
        return any([
            node.data == value,
            contains(node.left, value),
            contains(node.right, value)
            ])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)