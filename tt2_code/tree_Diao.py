"""
A tree ADT from Eagle Diao
"""
from typing import List, Any


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    value: int
    children: List[Any]

    def __init__(self, value, children=None):
        self.value = value
        self.children = children.copy() if children else []

    def _get_leaf_count(self):
        if not self.children:
            return 1
        else:
            return sum(
                child.leaf_count
                for child in self.children
                )

    leaf_count = property(_get_leaf_count)

    def _get_height(self):
        if not self.children:
            return 1
        else:
            return 1 + max(child.height for child in self.children)

    height = property(_get_height)

    def _get_max_value(self):
        if not self.children:
            return self.value
        else:
            return max(self.value, \
                       max(child.max_value for child in self.children))

    max_value = property(_get_max_value)

    def _get_sum_value(self):
        if not self.children:
            return self.value
        else:
            return self.value + sum(child.sum_value for child in self.children)

    sum_value = property(_get_sum_value)

    def _get_all_values(self):
        if not self.children:
            return [self.value]
        else:
            L = [self.value]
            for child in self.children:
                L.extend(child.all_values)
            return L

    all_values = property(_get_all_values)

    def has_value(self, v):
        if not self.children:
            return self.value == v
        else:
            return self.value == v or \
                   any(child.has_value(v) for child in self.children)

    def count_value(self, v):
        if not self.children:
            if self.value == v:
                return 1
            else:
                return 0
        else:
            n = 0
            if self.value == v:
                n = 1
            return n + sum(child.count_value(v) for child in self.children)

    def _get_sum_value_loop(self):
        total = 0
        q = [self]
        while q:
            t = q.pop(0)
            total += t.value
            if t.children:
                q.extend(t.children)
        return total



if __name__ == "__main__":
    t = Tree(5, [Tree(1), Tree(2), Tree(3, [Tree(1), Tree(2), Tree(8)])])
    print(t.leaf_count)
    print(t.height)
    print(t.max_value)
    print(t.sum_value)
    print(t.has_value(2))
    print(t.has_value(7))
    print(t.count_value(2))
    print(t._get_sum_value_loop())
    print(t.all_values)

