import unittest

from count_leaves_solution import count_leaves
from hypothesis import given
from hypothesis.strategies import recursive
from hypothesis.strategies import booleans
from hypothesis.strategies import tuples
from hypothesis.strategies import none

class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
   === Attributes ===
    @param object value: value in this node of tree
    @param BinaryTree|None left: left child
    @param BinaryTree|None right: right child
    @rtype: None
    """


    def __init__(self, value, left=None, right=None):
        """
        Create BinaryTree self with value and children left and right.
        @param BinaryTree self: this binary tree
        @param object value: value of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.value, self.left, self.right = value, left, right

def tuples_to_tree(t):
    """
    Return a BinaryTree generated from t and the number of leaves.

    Precondition: t is in the form (value, left child, right child) where
                  left child and right child are either None, a value, or
                  another tuple.

    @param tuple(bool, tuple|None|bool, tuple|None|bool) t: The tuple to turn
                                                            into a BinaryTree
    @rtype: (BinaryTree, int)
    """
    if t is None:
        return (None, 0)

    if type(t) == bool:
        return (BinaryTree(t), 1)

    (left, l_count) = tuples_to_tree(t[1])
    (right, r_count) = tuples_to_tree(t[2])
    num_leaves = l_count + r_count

    if num_leaves == 0:
        num_leaves = 1

    return (BinaryTree(t[0], left, right), num_leaves)

class CountLeavesTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test count_leaves to make sure it returns an int.
        """
        return_type = type(count_leaves(BinaryTree(1)))

        self.assertEqual(return_type, int, "count_leaves should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_none(self):
        """
        Test count_leaves on None.
        """
        self.assertEqual(count_leaves(None), 0, "count_leaves on None should " +
                         "return 0.")

    def test_leaf(self):
        """
        Test count_leaves on a leaf.
        """
        self.assertEqual(count_leaves(BinaryTree(1)), 1, "count_leaves should" +
                         " return 1 when used on a leaf.")

    def test_one_left_child(self):
        """
        Test count_leaves on a BinaryTree with one left child.
        """
        t = BinaryTree(1, BinaryTree(2))
        self.assertNotEqual(count_leaves(t), 2, "count_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertEqual(count_leaves(t), 1, "count_leaves should return 1 " +
                         "when used on a BinaryTree with only one child, " +
                         "where the child is a leaf.")

    def test_one_right_child(self):
        """
        Test count_leaves on a BinaryTree with one right child
        """
        t = BinaryTree(1, None, BinaryTree(2))
        self.assertNotEqual(count_leaves(t), 2, "count_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertEqual(count_leaves(t), 1, "count_leaves should return 1 " +
                         "when used on a BinaryTree with only one child, " +
                         "where the child is a leaf.")

    def test_two_leaf_children(self):
        """
        Test count_leaves on a BinaryTree with two leaf children.
        """
        t = BinaryTree(1, BinaryTree(2), BinaryTree(3))
        self.assertEqual(count_leaves(t), 2, "count_leaves should count all " +
                         "of the leaves in the entire BinaryTree.")

    @given(recursive(none() | booleans(), lambda children: tuples(booleans(),
                                                                  children,
                                                                  children)))
    def test_count_leaves(self, tuple_tree):
        """
        Test count_leaves on a randomly generated BinaryTree.
        """
        (t, expected) = tuples_to_tree(tuple_tree)
        actual = count_leaves(t)
        self.assertEqual(actual, expected,
                         ("test_count_leaves on BinaryTree\n{}\nReturned {}" +
                          " instead of {}.").format(tuple_tree, actual,
                                                    expected))

if __name__ == '__main__':
    unittest.main()
