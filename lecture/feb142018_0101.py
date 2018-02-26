from typing import List


def sum_list(list_: List[int]) -> int:
    """
    >>> sum_list([1, [2, 3], [4, 5, [6, 7], 8]])
    36
    >>> sum([])
    0
    """
    if not isinstance(list_, list):
        return list_
    else:
        return sum([sum_list(sublist) for sublist in list_])
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()