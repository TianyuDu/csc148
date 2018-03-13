from csc148_queue import Queue
from typing import List, Callable, Union, Any


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    def __init__(self, value: object=None, children: List['Tree']=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        # NEVER have a mutable default parameter...
        self.children = children.copy() if children else []

    def __repr__(self) ->str:
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.
        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('{}({}, {})'.format(self.__class__.__name__,
                                    repr(self.value),
                                    repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other: 'Tree') ->bool:
        """
        Return whether this Tree is equivalent to other.
        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent: int=0) -> str:
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual in indent: amount to indent
        each level of tree
        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
           23
        19
           17
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
              23
           19
              17
        29
           31
        """
        root_str = indent * " " + str(self.value)
        mid = len(self.non_none_kids()) // 2
        left_str = [c.__str__(indent + 3)
                    for c in self.non_none_kids()][: mid]
        right_str = [c.__str__(indent + 3)
                     for c in self.non_none_kids()][mid:]
        return '\n'.join(right_str + [root_str] + left_str)

    def height(self) ->int:
        """
        Return length of longest path, + 1, in tree rooted at self.

        >>> t = Tree(5)
        >>> t.height()
        1
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> t.height()
        3
        """
        if self.children == []:
            return 1
        else:
            return 1 + max([c.height() for c in self.children])
        # another solution
        # return 1 + max([c.height() for c in self.children]+[0])

    def leaf_count(self) -> int:
        """
        Return the number of leaves in Tree t.
        >>> t = Tree(7)
        >>> t.leaf_count()
        1
        >>> t = descendants_from_list(Tree(7),[0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> t.leaf_count()
        6
        """
        if self.children == []:
            return 1
        else:
            return sum([x.leaf_count() for x in self.children])

    def is_leaf(self):
        """Return whether Tree self is a leaf
        @param Tree self:
        @rtype: bool
        >>> Tree(5).is_leaf()
        True
        >>> Tree(5,[Tree(7)]).is_leaf()
        False
        """
        return len(self.children) == 0

    def non_none_kids(self):
        """ Return a list of Tree self's non-None children.

        @param Tree self:
        @rtype: list[Tree]
        """
        return [c
                for c in self.children
                if c is not None]

    def flatten(self) -> List:
        """ Return a list of all values in tree rooted at self.
        >>> t = Tree(5)
        >>> t.flatten()
        [5]
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> L = t.flatten()
        >>> L.sort()
        >>> L == [0, 1, 3, 5, 7, 7, 9, 11, 13]
        True
        """
        if self.children == []:
            return [self.value]
        else:
            return ([self.value]
                    + sum([c.flatten()
                           for c in self.children], []))

# helpful helper function


def descendants_from_list(t, list_, arity):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int arity: maximum branching factor
    @rtype: Tree

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
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


def preorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of Tree t in preorder, and act on the nodes
    as they are visited.
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> preorder_visit(t, act)
    0
    1
    4
    5
    6
    2
    7
    3
    """
    act(t)
    for child in t.children:
        preorder_visit(child, act)


def postorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> postorder_visit(t, act)
    4
    5
    6
    1
    7
    2
    3
    0
    """
    for child in t.children:
        postorder_visit(child, act)
    act(t)


# def visit_level(t: Tree, act: Callable) -> None:
#     to_act = Queue()
#     to_act.add(t)
#     while not to_act.isempty():
#         tree = to_act.remove()
#         act(tree)
#         for child in tree.childrern:
#             to_act.add(child)
#
#
# def visit_level2(t: Tree, act: Callable([Tree], Any), n: int) -> int:
#     if n == 0:
#         act(t)
#         return 1
#     else:
#         return sum([visit_level2(child, act, n - 1) for child in t.children])
    # level_to_visit = 0
    # visited = 1
    # while visited > 0:
    #     visited = visit_level2(t, act, level_to_visit)
    #     level_to_visit += 1

################################################
#### The following are Module functions
#### they are commented becuase we implemented
#### a class methods instead of them
# def leaf_count(t: Tree) -> int:
#     """
#     Return the number of leaves in Tree t.
#     >>> t = Tree(7)
#     >>> leaf_count(t)
#     1
#     >>> t = descendants_from_list(Tree(7),[0, 1, 3, 5, 7, 9, 11, 13], 3)
#     >>> leaf_count(t)
#     6
#     """
#     if t.children==[]:
#         return 1
#     else:
#         return sum([leaf_count(x) for x in t.children])
#     # if t.children!=[]:
#     #     return sum([leaf_count(x) for x in t.children])
#     # else:
#     #     return 1
# def height(t: Tree) -> int:
#     """
#     Return 1 + length of longest path of t.
#     >>> t = Tree(13)
#     >>> height(t)
#     1
#     >>> t = descendants_from_list(Tree(13),[0, 1, 3, 5, 7, 9, 11, 13], 3)
#     >>> height(t)
#     3
#     """
#     # 1 more edge than the maximum height of a child, except
#     # what do we do if there are no children?
#     # helpful helper function
#     if t.children ==[]:
#         return 1
#     else:
#         return 1 + max([height(x) for x in t.children])
#
# def arity(t: Tree) -> int:
#     """
#     Return the maximum branching factor (arity) of Tree t.
#     >>> t = Tree(23)
#     >>> arity(t)
#     0
#     >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
#     >>> tn3 = Tree(3, [Tree(6), Tree(7)])
#     >>> tn1 = Tree(1, [tn2, tn3])
#     >>> arity(tn1)
#     4
#     """
#     if t.children ==[]:
#         return 0
#     else:
#         y= [arity(x) for x in t.children]
#         return max(y) if max(y)>len(y) else len(y)
#     # -- another solution
#     # if t.children ==[]:
#     #     return 0
#     # else:
#     #     return max(len(t.children),max([arity(x) for x in t.children]))
#     # -- another solution
#     # if t.children ==[]:
#     #     return 0
#     # else:
#     #     return max([arity(x) for x in t.children]+[len(t.children)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
