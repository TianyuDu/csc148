"""
Some module level function to run on
BTNodes and a BST
"""
from bst import BST, BTNode
from typing import Union, Callable, Any
from csc148_queue import Queue


def height(node: Union[BTNode, None]) -> int:
    """
    Return height of tree rooted at node.

    >>> height(None)
    0
    >>> height(BTNode(5, BTNode(3), BTNode(7)))
    2
    """
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))


def find(node: Union[BTNode, None],
         data: object) -> Union[BTNode, None]:
    """

    Return a BTNode containing data, or else None.

    >>> find(None, 15) is None
    True
    >>> b = BTNode(5, BTNode(4))
    >>> find(b, 7) is None
    True
    >>> find(b, 4)
    BTNode(4, None, None)
    """
    if node is None:
        pass
    else:
        find_left_result = find(node.left, data)
        if node.data == data:
            return node
        elif find_left_result is not None:
            return find_left_result
        else:
            return find(node.right, data)


def evaluate(b: BTNode) -> float:
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float data.  Otherwise, evaluate b.left and
    b.right and combine them with b.data.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    >>> b = BTNode(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BTNode('*', BTNode(3.0), BTNode(4.0))
    >>> evaluate(b)
    12.0
    """
    # leaf?
    b.data: Union[str, float]
    if b.left is None and b.right is None:
        return b.data
    # produce the string expression, then evaluate it
    else:
        return eval("{} {} {}".format(evaluate(b.left),
                                      b.data,
                                      evaluate(b.right)))


def parenthesize(b: BTNode) -> str:
    """
    Parenthesize the expression rooted at b, so that float data is
    not parenthesized, but each pair of expressions
    joined by an operator are parenthesized.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    >>> b = BTNode(3.0)
    >>> print(parenthesize(b))
    3.0
    >>> b = BTNode('+', BTNode('*', BTNode(3.0), BTNode(4.0)), BTNode(7.0))
    >>> print(parenthesize(b))
    ((3.0 * 4.0) + 7.0)
    """
    # leaf?
    # if left is missing so must the right!
    if b.left is None:
        return str(b.data)
    # general expression...
    else:
        return "({} {} {})".format(parenthesize(b.left),
                                 b.data,
                                 parenthesize(b.right))

def list_between(node: Union[BTNode, None], start: int, end: int) -> list:
    """
    Return a Python list of all values in the binary search tree
    rooted at node that are between start and end (inclusive).

    >>> b = BTNode(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """


def list_internal_between(node: Union[BTNode, None], start: int, end: int) -> list:
        """
        Return a Python list of the data from all internal nodes of
        the tree rooted at node that are between start and end,
        inclusive.

        >>> list_internal_between(None, 4, 7)
        []
        >>> b = BTNode(8)
        >>> b = insert(b, 4)
        >>> b = insert(b, 2)
        >>> b = insert(b, 6)
        >>> b = insert(b, 12)
        >>> b = insert(b, 14)
        >>> b = insert(b, 10)
        >>> L = list_internal_between(b, 3, 13)
        >>> L.sort()
        >>> L
        [4, 8, 12]
        """


def list_longest_path(node: Union[BTNode, None]) -> list:
    """
    List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> list_longest_path(BTNode(5, BTNode(3, BTNode(2), None), BTNode(7)))
    [5, 3, 2]
    """


def is_leaf(node):
    """ (BTNode) -> bool

    Return whether nodeis a leaf.

    >>> b = BTNode(1, BTNode(2))
    >>> is_leaf(b)
    False
    >>> is_leaf(b.left)
    True
    """
    return not node.left and not node.right


def inorder_visit(b: Union[BTNode, None],
                  visit: Callable[[BTNode], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in order.

    >>> b = BTNode("A", BTNode("C"), BTNode("D"))

    >>> def f(node): print(node.data)
    >>> inorder_visit(b, f)
    C
    A
    D
    """
    if b is not None:
        inorder_visit(b.left, visit)
        visit(b)
        inorder_visit(b.right, visit)


def preorder_visit(b: Union[BTNode, None],
                   visit: Callable[[BTNode], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in preorder
    and perform effect.


    >>> b = BTNode("A", BTNode("C"), BTNode("D"))

    >>> def f(node): print(node.data)
    >>> preorder_visit(b, f)
    A
    C
    D
    """
    # if root is None, do nothing
    if b is None:
        pass
    else:
        visit(b)
        preorder_visit(b.left, visit)
        preorder_visit(b.right, visit)


def postorder_visit(b: Union[BTNode, None],
                    visit: Callable[[BTNode], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in postorder
    and perform effect.

    >>> b = BTNode("A", BTNode("C"), BTNode("D"))

    >>> def f(node): print(node.data)
    >>> postorder_visit(b, f)
    C
    D
    A
    """
    # if b is None, do nothing...
    if b is not None:
        postorder_visit(b.left, visit)
        postorder_visit(b.right, visit)
        visit(b)
    # do nothing if b *is* None


def levelorder_visit(b: Union[BTNode, None],
                     visit: Callable[[BTNode], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in level order.

    If tree rooted at root is empty, do nothing.

    >>> b = BTNode("A", BTNode("C", BTNode("B")), BTNode("D"))

    >>> def f(node): print(node.data)
    >>> levelorder_visit(b, f)
    A
    C
    D
    B
    """
    if b is None:
        pass
    else:
        q = Queue()
        q.add(b)
        while not q.is_empty():
            n = q.remove()
            visit(n)
            if n.left is not None:
                q.add(n.left)
            if n.right is not None:
                q.add(n.right)


def find_max(node: BTNode) -> BTNode:
    """
    Find and return node with maximum data, assume node is not None.

    Assumption: node is the root of a binary search tree.

    >>> find_max(BTNode(5, BTNode(3), BTNode(7)))
    BTNode(7, None, None)
    """
    return find_max(node.right) if node.right else node


def insert(node, data):
    """ (BTNode, object) -> BTNode

    Insert data in BST rooted at node if necessary, and return new root.

    >>> b = BTNode(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """


def contains(node, value):
    """ (BTNode, object) -> value

    Return whether tree rooted at node contains value.

    >>> contains(None, 5)
    False
    >>> contains(BTNode(5, BTNode(7), BTNode(9)), 7)
    True
    """
    if node is None:
        return False
    else:
        return (node.data == value or
                contains(node.left, value) or
                contains(node.right, value))


def delete(node, data):
    """ (BTNode, object) -> BTNode:

    Delete node containing data, if it exists, and return resulting tree.

        >>> b = BTNode(8)
        >>> b = insert(b, 4)
        >>> b = insert(b, 2)
        >>> b = insert(b, 6)
        >>> b = insert(b, 12)
        >>> b = insert(b, 14)
        >>> b = insert(b, 10)
        >>> b = delete(b, 12)
        >>> print(b)
                14
            10
        8
                6
            4
                2
        <BLANKLINE>
        >>> b = delete(b, 14)
        >>> print(b)
            10
        8
                6
            4
                2
        <BLANKLINE>
    """
    # Algorithm for delete:
    # 1. If this node is None, return that
    # 2. If data is less than node.data, delete it from left child and
    #     return this node
    # 3. If data is more than node.data, delete it from right child
    #     and return this node
    # 4. If node with data has fewer than two children,
    #     and you know one is None, return the other one
    # 5. If node with data has two non-None children,
    #     replace data with that of its largest child in the left subtree,
    #     and delete that child, and return this node
    return_node = node


if __name__ == '__main__':
    import doctest
    doctest.testmod()
