from typing import Union

## Please note depth 0 of a nested list is the root
## hence the width of depth 0 is always 1

## For example, if we have an object [1, [2, 3], 4]
## at depth 0, the object is just a list [1, [2, 3], 4] so it's width is 1
## at depth 1, the objects are 1, [2, 3], 4, width is 3 (we count both number and list)
## at depth 2, the objects are 2, 3, width is 2

def width_at(list_: Union[list, object], d: int) -> int:
    """
    >>> obj = [1, 2, 3]
    >>> width_at(obj, 0)
    1
    >>> obj = [[1, 2], [2], [1, [3, 4]]]
    >>> width_at(obj, 0)
    1
    >>> width_at(obj, 1)
    3
    >>> width_at(obj, 2)
    5
    """

    if d == 0:
        return 1
    if isinstance(list_, list):
        return sum([width_at(x, d - 1) for x in list_])
    else:
        return 0


def width(list_: Union[list, object], max_depth: int)-> int:
    """ Return the maximum number of items that occur at the same depth in list_
    or its sub-lists combined. These could be list or non-list items.
    Elements may be lists or non-lists.

    >>> list_ = [0, 1]
    >>> width(list_, 1)
    2
    >>> list_ = [[0, 1], 2, [3, [[], 4]]]
    >>> width(list_, 4) # 4 elements: 0, 1, 3, [[] , 4]
    4
    """
    pass


def divrem(a: int, b: int) -> tuple:
    """ Return the quotient q and the remainder r of a divided by b,
        as in a = qb + r, where 0 <= r < b.
        Precondition: a, b are non-negative.

        divrem(3, 0) # throws an error

    >>> divrem(16, 6) # 16 = 2*6+4
    (2, 4)
    >>> divrem(12, 4) # 12 = 3*4+0
    (3, 0)
    """
    pass


def sum_only_num(obj: Union[list, object]) -> int:
    """ Returns the sum of all the numbers in the nested list
    >>> sum_only_num([1, 2, "a"])
    3
    >>> sum_only_num([[1, 2], [2, "a"], "ok", False, [2, [[2]]]])
    9
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()