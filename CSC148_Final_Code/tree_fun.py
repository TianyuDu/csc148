from typing import List, Callable, Any


class Tree:
    value: int
    children: List['Tree']

    def __init__(self, value: int, children=None):
        self.value = value
        self.children = children.copy() if children else []

    def __eq__(self, other: object):
        return type(self) == type(other) and \
               self.children == other.children

    def __repr__(self):
        return "Tree({}, {})".format(self.value, self.children)

    # Walk through the whole Tree w/o Callable

    def preorder(self):
        """
        Print each value in this Tree using pre-order.
        order of children is left to right.
        >>> tn2 = Tree(2, [Tree(4), Tree(4.5)])
        >>> tn3 = Tree(3, [Tree (6), Tree(7)])
        >>> tn1 = Tree(10, [tn2, tn3, Tree(50)])
        >>> tn1.preorder()
        10
        2
        4
        4.5
        3
        6
        7
        50
        """
        print(self.value)
        for c in self.children:
            c.preorder()

    # Walk through the whole Tree w/ Callable

    def preorder_with_predicate(self, predicate: Callable[[int], bool]):
        """
        Print values in this Tree using pre-order that meet <predicate>.
        order of children is left to right.
        >>> tn2 = Tree(2, [Tree(4), Tree(4.5)])
        >>> tn3 = Tree(3, [Tree (6), Tree(7)])
        >>> tn1 = Tree(10, [tn2, tn3, Tree(50)])
        >>> def predicate(v): return v > 4
        >>> tn1.preorder_with_predicate(predicate)
        10
        4.5
        6
        7
        50
        """
        if predicate(self.value):
            print(self.value)
        for c in self.children:
            c.preorder_with_predicate(predicate)

    def all_add_one(self):
        """
        Mutate this tree so that each value is added one.
        >>> c1 = Tree(2, [Tree(3), Tree(4), Tree(5)])
        >>> t = Tree(15, [c1, Tree(6), Tree(7)])
        >>> t.all_add_one()
        >>> t
        Tree(16, [Tree(3, [Tree(4, []), Tree(5, []), Tree(6, [])]), Tree(7, []), Tree(8, [])])
        """
        self.value += 1
        for c in self.children:
            c.all_add_one()

    def destructive_map(self, transform: Callable[[int], Any]):
        """
        Mutate this tree so that each value is transformed by <transform>
        >>> c1 = Tree(2, [Tree(3), Tree(4), Tree(5)])
        >>> t = Tree(15, [c1, Tree(6), Tree(7)])
        >>> def trans(x): return x * 2
        >>> t.destructive_map(trans)
        >>> t
        Tree(30, [Tree(4, [Tree(6, []), Tree(8, []), Tree(10, [])]), Tree(12, []), Tree(14, [])])
        """
        self.value = transform(self.value)
        for c in self.children:
            c.destructive_map(transform)

    def map(self, transform: Callable[[int], Any]):
        """
        Produces a new Tree so that every value will be
        transformed by <transform>.

        >>> c1 = Tree(2, [Tree(3), Tree(4), Tree(5)])
        >>> t = Tree(15, [c1, Tree(6), Tree(7)])
        >>> def trans(x): return x * 2
        >>> t.map(trans)
        Tree(30, [Tree(4, [Tree(6, []), Tree(8, []), Tree(10, [])]), Tree(12, []), Tree(14, [])])
        """
        return Tree(transform(self.value), [c.map(transform) for c in self.children])

    def stat(self):
        """
        Mutate each value in this Tree so that each value is now the number of children.
        >>> c1 = Tree(2, [Tree(3), Tree(4), Tree(5)])
        >>> t = Tree(15, [c1, Tree(6), Tree(7)])
        >>> t.stat()
        >>> t
        Tree(3, [Tree(3, [Tree(0, []), Tree(0, []), Tree(0, [])]), Tree(0, []), Tree(0, [])])
        """
        if isinstance(self.children, list):
            self.value = len(self.children)
        else:
            self.value = 0
        for c in self.children:
            c.stat()
    # Depth Related

    def sum_at_depth(self, depth):
        """ Returns the sum of all the values at given d

        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.sum_at_depth(0)
        17
        >>> t.sum_at_depth(1)
        5
        >>> t.sum_at_depth(2)
        12
        >>> t.sum_at_depth(3)
        14
        >>> t.sum_at_depth(4)
        0
        """
        if depth == 0:
            return self.value
        return sum([
            c.sum_at_depth(depth-1)
            for c in self.children
        ])

    def list_at_depth(self, depth):
        """ Returns the list of all the values at given d

        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.list_at_depth(0)
        [17]
        >>> t.list_at_depth(1)
        [-2, 3, 4]
        >>> t.list_at_depth(2)
        [5, 6, -7, 8]
        >>> t.list_at_depth(3)
        [-8, 13, 9]
        >>> t.list_at_depth(4)
        []
        """
        if depth == 0:
            return [self.value]
        return sum([
            c.list_at_depth(depth - 1)
            for c in self.children
        ], [])

    # Path related

    def longest_path(self):
        """ Returns a list of items on the longest possible path between the
            root of the tree and one of its leaves. The list is ordered by
            increasing depth, so the tree’s root is always the first element.

        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.longest_path()
        [17, 3, 8, 9]
        """
        collection = self.all_path()
        collection.sort(key=lambda x: len(x))
        return collection[-1]

    def all_path(self):
        """
        returns a list of list of items on all possible path between the root
        of the tree and one of its leaves. Each list in returned list is ordered
        by increasing depth, so the tree’s root is always the first element, and
        returned list of list can be in any order

        >>> t = Tree(17, [Tree(-2, [Tree(5), Tree(6, [Tree(-8), Tree(13)])]), Tree(3, [Tree(-7), Tree(8, [Tree(9)])]), Tree(4)])
        >>> t.all_path()
        [[17, -2, 5], [17, -2, 6, -8], [17, -2, 6, 13], [17, 3, -7], [17, 3, 8, 9], [17, 4]]
        """
        if self.children == []:  # Base case
            return [[self.value]]
        return [
            [self.value] + sub_path
            for c in self.children
            for sub_path in c.all_path()
        ]
