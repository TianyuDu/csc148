import unittest

from concatenate_leaves_solution import concatenate_leaves
from hypothesis import given
from hypothesis.strategies import recursive
from hypothesis.strategies import text
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

    @param tuple(bool, tuple|None|int, tuple|None|int) t: The tuple to turn
                                                            into a BinaryTree
    @rtype: (BinaryTree, int)
    """
    if t is None:
        return (None, '')

    if type(t) == str:
        return (BinaryTree(t), t)

    (left, l_count) = tuples_to_tree(t[1])
    (right, r_count) = tuples_to_tree(t[2])
    concatenate_leaves = l_count + r_count

    if not left and not right:
        concatenate_leaves = t[0]

    return (BinaryTree(t[0], left, right), concatenate_leaves)

class ConcatenateLeavesTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test concatenate_leaves to make sure it returns an int.
        """
        return_type = type(concatenate_leaves(BinaryTree("a")))

        self.assertEqual(return_type, str,
                         "concatenate_leaves should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_none(self):
        """
        Test concatenate_leaves on None.
        """
        self.assertEqual(concatenate_leaves(None), "",
                         "concatenate_leaves on None should " +
                         "return ''.")

    def test_leaf(self):
        """
        Test concatenate_leaves on a leaf.
        """
        self.assertEqual(concatenate_leaves(BinaryTree("a")), "a",
                         "concatenate_leaves should" +
                         " return the leaf's value when used on a leaf.")

    def test_one_left_child(self):
        """
        Test concatenate_leaves on a BinaryTree with one left child.
        """
        t = BinaryTree("a", BinaryTree("b"))
        self.assertNotEqual(concatenate_leaves(t), "ab",
                            "concatenate_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertNotEqual(concatenate_leaves(t), "a",
                            "concatenate_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertEqual(concatenate_leaves(t), "b",
                         "concatenate_leaves should return the " +
                         "value of the leaf child when used on a BinaryTree " +
                         "with a single leaf child.")

    def test_one_right_child(self):
        """
        Test concatenate_leaves on a BinaryTree with one right child
        """
        t = BinaryTree("a", None, BinaryTree("b"))
        self.assertNotEqual(concatenate_leaves(t), "ab",
                            "concatenate_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertNotEqual(concatenate_leaves(t), "a",
                            "concatenate_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertEqual(concatenate_leaves(t), "b",
                         "concatenate_leaves should return the " +
                         "value of the leaf child when used on a BinaryTree " +
                         "with a single leaf child.")

    def test_two_leaf_children(self):
        """
        Test concatenate_leaves on a BinaryTree with two leaf children.
        """
        t = BinaryTree("a", BinaryTree("b"), BinaryTree("c"))
        self.assertEqual(concatenate_leaves(t), "bc",
                         "concatenate_leaves should sum all " +
                         "of the leaves in the entire BinaryTree.")

    @given(recursive(none() | text(max_size=3),
                     lambda children: tuples(text(max_size = 3),
                                             children,
                                             children))
           )
    def test_concatenate_leaves(self, tuple_tree):
        """
        Test concatenate_leaves on a randomly generated BinaryTree.
        """
        (t, expected) = tuples_to_tree(tuple_tree)
        actual = concatenate_leaves(t)
        self.assertEqual(actual, expected,
                         ("test_concatenate_leaves on BinaryTree\n{}" +
                          "\nReturned {}" +
                          " instead of {}.").format(tuple_tree, actual,
                                                    expected))

if __name__ == '__main__':
    unittest.main()
