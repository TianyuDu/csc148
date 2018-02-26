"""
Lecture note 0101
Feb 16 2018
"""

from typing import List

class Tree:
    def __init__(self, value: object=None, children: List[Tree]=None) -> None:
        self.value = value  # root value
        self.childrne = children[:] if children is not None else []
        
    

def leaf_count(t: Tree) -> int:
    """
    Count number of leaves.
    
    >>> t = Tree(7)
    >>> leaf_count(t)
    7
    """
    if t.children == []:
        return 1
    else:
        return sum([leaf_count(child) for child in t.children])
        
        
def height(t: Tree):
    """
    >>> t = Tree(3)
    >>> height(t)
    1
    """
    if len(t.children) == 0:
        return 1
    else:
        return 1 + max([height(c) for c in t.children])


def branching_factor(t: Tree):
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod