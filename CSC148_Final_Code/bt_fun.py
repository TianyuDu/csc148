from typing import Optional, Union, Any, List


class BTNode:
    """Binary Tree node.
    """
    # The item stored at the root of the tree, or None if the tree is empty
    data: object
    # The left subtree, or None if the tree is empty
    left: Optional['BTNode']
    # The right subtree, or None if the tree is empty
    right: Optional['BTNode']

    def __init__(self, data: object,
                 left: Union["BTNode", None] = None,
                 right: Union["BTNode", None] = None) -> None:
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

    def __str__(self, indent: str = "") -> str:
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

# You are required to implements the following functions


def count_leaves(root: Union[BTNode, None]):
    """ Return the number of leaves in the tree rooted at root.
    (2017)
    >>> count_leaves(None)
    0
    >>> count_leaves(BTNode(0))
    1
    >>> t1 = BTNode(1, BTNode(3), None)
    >>> t2 = BTNode(2, BTNode(4), BTNode(5))
    >>> count_leaves(BTNode(0, t1, t2))
    3
    """
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def count_single_parent(root: Union[BTNode, None]):
    """ Return the number of internal nodes in the tree that
    has only one child
    (2017)
    >>> count_single_parent(None)
    0
    >>> count_single_parent(BTNode(0))
    0
    >>> t1 = BTNode(1, BTNode(3), None)
    >>> count_single_parent(t1)
    1
    >>> t2 = BTNode(2, BTNode(4), BTNode(5))
    >>> count_single_parent(BTNode(0, t1, t2))
    1
    """
    if root is None:
        return 0
    if (root.left is None) ^ (root.right is None):
        return 1
    return count_single_parent(root.left) + count_single_parent(root.right)


def make_full(t: Union[BTNode, None]) -> int:
    """
    A full binary tree is a tree in which every node other
    than the leaves has two children. Complete the function
    make_full that takes a binary tree t and returns the
    minimum number of nodes required to make it a full binary tree.
    You may define helper functions as needed.
    If you define helper functions, please do provide
    docstrigs (no doctests required).
    (2017)

    Return the minimum number of nodes required to make
    t a full binary tree.

    >>> make_full(None)
    0
    >>> t = BTNode(10, BTNode(30, BTNode(50), None), BTNode(40))
    >>> make_full(t)
    1
    """
    if t is None:
        return 0
    if (t.left is None) ^ (t.right is None):
        return 1
    return make_full(t.left) + make_full(t.right)


def is_siblings(t: Union[BTNode, None], item1: int, item2: int):
    """
    Siblings in a Binary Tree means two nodes share the same parent.

    Return True if given items <item1> and <item2> are siblings
    given binary tree, False otherwise.

    >>> is_siblings(None, 1, 2)
    False
    >>> t = BTNode(10, BTNode(30, BTNode(50), None), BTNode(40))
    >>> is_siblings(t, 10, 30)
    False
    >>> is_siblings(t, 30, 40)
    True
    >>> is_siblings(t, 50, 40)
    False
    """
    if t is None:
        return False
    if t.left is None or t.right is None:
        return False
    if (t.left.data == item1 and t.right.data == item2) or (t.right.data == item1 and t.left.data == item2):
        return True
    return is_siblings(t.left, item1, item2) or is_siblings(t.right, item1, item2)


def is_ancestor_of(t: Union[BTNode, None], a: int, d: int):
    """
    if one node A is ancestor of another node B in a binary tree
    it means B is either child of A, or child of child of A, and
    so long, as long as B is directly from A.
    Hint: you may want to consider write a helper
     that is very similar to the bst_find function
    defined below (in bt_fun.py)

    Return True if <a> is ancestor of <d> in given binary
    search tree <t>

    >>> is_ancestor_of(None, 1, 2)
    False
    >>> t = BTNode(10, BTNode(5, BTNode(3), None), BTNode(40))
    >>> is_ancestor_of(t, 10, 5)
    True
    >>> is_ancestor_of(t, 10, 3)
    True
    >>> is_ancestor_of(t, 5, 40)
    False
    """
    if t is None:
        return False
    if t.data == a:  # If current node is the target ancestor, run the CONFIRM method.
        return is_decentor(t, d)
    else:  # If not, keep looking.
        return is_ancestor_of(t.left, a, d) or is_ancestor_of(t.right, a, d)


def is_decentor(t, d):
    """
    Return if any decentor of t contains value d
    """
    if t is None:  # Base case
        return False
    return (t.data == d) or is_decentor(t.left, d) or is_decentor(t.right, d)


def swap_even(t: BTNode, depth: int=0) -> None:
    """Swap left and right children of nodes at even depth.
    Recall that the root has depth 0, its children have depth 1,
    grandchildren have depth 2, and so on. If a node only has
    one child, do not swap anything.
    (2016)

    >>> bl = BTNode(1, BTNode(2, BTNode(3)))
    >>> b4 = BTNode(4, BTNode(5), bl)
    >>> print(b4)
        1
            2
                3
    4
        5
    <BLANKLINE>
    >>> swap_even(b4)
    >>> print(b4)
        5
            2
                3
    4
        1
    <BLANKLINE>
    """
    if depth % 2 == 0 and t is not None:  # Make sure the tree is not None.
        # Check if the children if it is at even level.
        if t.left is not None and t.right is not None:  # Make sure that this node has two children.
            t.left.data, t.right.data= t.right.data, t.left.data
        swap_even(t.left, depth+1)
        swap_even(t.right, depth+1)


def sum_until_height(t: Union[BTNode, None], until: int):
    """
    Produce the sum of all the nodes until given height
    if <until> is 0 the result is always 0
    >>> bl = BTNode(1, BTNode(2, BTNode(3)))
    >>> b4 = BTNode(4, BTNode(5), bl)
    >>> sum_until_height(b4, 0)
    0
    >>> sum_until_height(b4, 1)
    4
    >>> sum_until_height(b4, 2)
    10
    >>> sum_until_height(b4, 3)
    12
    """
    if until == 0 or t is None:
        return 0
    return int(t.data if t is not None else 0) + sum_until_height(t.left, until - 1) + sum_until_height(t.right, until - 1)

# A left streak is defined as a sequence of three or
# more nodes on the leftmost side of the tree where
# none of the nodes in the sequence have a right child.
#  A property of a left streak is that it can be broken
#  to reduce the height of the tree by 1, while
#  maintaining the binary search tree property.
# The streak parent is the node whose left child is the
# shallowest (closest to the root) node in the streak.
# (2017)

# find_left_streak is a helper function that is
# implemented for you to solve fix_left_streaks


def find_left_streak(t: BTNode) -> Union[BTNode, None]:
    """ Return the parent node of the shallowest left streak in t,
    or None if there is no left streak.
    Assume t is the root of the whole tree

    >>> left = BTNode(4, (BTNode(3, BTNode(2, BTNode(1, BTNode(0))))))
    >>> t = BTNode(5, left, BTNode(6))
    >>> find_left_streak(t).data
    5
    >>> t.left.right = BTNode(4.5)
    >>> find_left_streak(t).data
    4
    """
    streak_parent = t
    while streak_parent.left is not None:
        node = streak_parent.left
        if (node.left is not None and node.right is None) and \
                (node.left.left is not None and node.left.right is None):
            return streak_parent
        streak_parent = node
    # if the end of the loop is reached,
    # there is no left streak - return None


def fix_left_streaks(t: BTNode) -> None:
    """ Modify t by fixing all left streaks.

    >>> left = BTNode(4, (BTNode(3, BTNode(2, BTNode(1, BTNode(0))))))
    >>> t = BTNode(5, left, BTNode(6))
    >>> print(t)
        6
    5
        4
            3
                2
                    1
                        0
    <BLANKLINE>
    >>> height(t)
    6
    >>> t.left.right is None
    True
    >>> t.left.left.right is None
    True
    >>> fix_left_streaks(t)
    >>> print(t)
        6
    5
            4
        3
                2
            1
                0
    <BLANKLINE>
    >>> height(t)
    4
    >>> t.left.right.data == 4
    True
    >>> t.left.left.right.data == 2
    True
    """
    while find_left_streak(t) is not None:
        start = find_left_streak(t)
        sub = start.left.left
        sub.right = start.left
        sub.right.left = None
        start.left = sub


# Following functions are already implemented, they are given here
# as a reference. (They are from this term's course note

# module level function to calculate height
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


# module level function to calculate the maximum node from the
# given node (BT), please note this is NOT binary search
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
        return None
    else:
        find_left_result = find(node.left, data)
        if node.data == data:
            return node
        elif find_left_result is not None:
            return find_left_result
        else:
            return find(node.right, data)


def bst_find(node: Union[BTNode, None], data: object) -> Union[BTNode, None]:
    """
    Return a BTNode containing data, or else None. node will be a BST.
    >>> find(None, 15) is None
    True
    >>> b = BTNode(5, BTNode(4))
    >>> find(b, 7) is None
    True
    >>> find(b, 4)
    BTNode(4, None, None)
    >>> b = BTNode(5, BTNode(4), BTNode(8))
    >>> find(b, 8)
    BTNode(8, None, None)
    """
    if node is None:
        return None
    if node.data == data:
        return node
    if data < node.data:
        return bst_find(node.left, data)
    else:
        return bst_find(node.right, data)


def find_max(node):
    """Return the maximum item in this BST root node, or None if this
       BST is empty.
    >>> find_max(None) is None
    True
    >>> b = BTNode(5, BTNode(4), BTNode(8))
    >>> find_max(b)
    8
    """
    if not node:
        return None
    if not node.right:
        return node.data
    else:
        return find_max(node.right)


def in_order_travel(node: Union[BTNode, None]) -> List[object]:
    """
    Extra practice
    >>> b = BTNode(5, BTNode(4), BTNode(8))
    >>> in_order_travel(b)
    [4, 5, 8]
    """
    if not node:
        return []
    return in_order_travel(node.left) + [node.data] + in_order_travel(node.right)
