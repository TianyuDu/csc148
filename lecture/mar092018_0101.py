from typing import Union, Optional
from bst import *
from bst_functions import *


def tree_add(node: Union[BTNode, None], num: int) -> Optional[BTNode]:
    """
    Return BTNode with value n.data + num for each BTNode n of tree rooted at
    node
    
    >>> tree_add(BTNode(1), 1)
    """
    if node is None:
        pass
    else:
        return BTNode(node.data + num, 
        tree_add(None, ))
        
def t(n):
    return BTNode(n, t())
    
    
def insert 