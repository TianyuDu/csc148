"""
"""


def height(node: BTNode) -> int:
    if node is None:
        return 0
    else:
        return 1 + max(
            height(node.left),
            height(node.right))
        

def find(node: BTNode, data: object) -> BTNode:
    """
    >>> b = BTNode(5, BTNode(4))
    >>> find(b, 7) is None
    True
    >>> find(b, 4)
    BTNode(4, None, None)
    """
    if node is None:
        return None
    elif node.value == data:
        return node
    elif find(node.left, data) is not None:
        return find(node.left, data)
    else:
        return find(node.right, data)
    
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)