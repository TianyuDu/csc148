""" recursion exercises with nested lists
"""
from typing import List, Union


def gather_lists(list_: List[List[object]]) -> List[object]:
    """
    Return the concatenation of the sublists of list_.

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # special form of sum for "adding" lists
    return sum(list_, [])


def list_all(obj: Union[list, object]) -> list:
    """
    Return a list of all non-list elements in obj or obj's sublists, if obj
    is a list.  Otherwise, return a list containing obj.

    >>> obj = 17
    >>> list_all(obj)
    [17]
    >>> obj = [1, 2, 3, 4]
    >>> list_all(obj)
    [1, 2, 3, 4]
    >>> obj = [[1, 2, [3, 4], 5], 6]
    >>> all([x in list_all(obj) for x in [1, 2, 3, 4, 5, 6]])
    True
    >>> all ([x in [1, 2, 3, 4, 5, 6] for x in list_all(obj)])
    True
    """

    ret_list = []
    if not isinstance(obj, list):
        return [obj]
    elif all([not isinstance(sublist, list) for sublist in obj]):
        return obj
    else:
        for sublist in obj:
            ret_list.extend(list_all(sublist))
    return ret_list

def max_length(obj: Union[list, object]) -> int:
    """
    Return the maximum length of obj or any of its sublists, if obj is a list.
    otherwise return 0.

    >>> max_length(17)
    0
    >>> max_length([1, 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    """
    if not isinstance(obj, list):
        return 0
    elif all([not isinstance(sublist, list) for sublist in obj]):
        return len(obj)
    else:
        return max([max_length(sublist) for sublist in obj])


def list_over(obj: Union[list, str], n: int) -> List[str]:
    """
    Return a list of strings of length greater than n in obj,
    or sublists of obj, if obj is a list.
    If obj is a string of length greater than n, return a list
    containing obj.  Otherwise return an empty list.

    >>> list_over("five", 3)
    ['five']
    >>> list_over("five", 4)
    []
    >>> list_over(["one", "two", "three", "four"], 3)
    ['three', 'four']
    """
    ret_list = []
    if not isinstance(obj, list):
        if len(obj) > n:
            return [obj]
    else:
        ret_list.extend(
            [list_over(subobj, n) for subobj in obj]
            )
    ret_list = [item for item in ret_list if item != []]
    ret_list = gather_lists(ret_list)
    return ret_list


def list_even(obj: Union[list, int]) -> List[int]:
    """
    Return a list of all even integers in obj,
    or sublists of obj, if obj is a list.  If obj is an even
    integer, return a list containing obj.  Otherwise return
    en empty list.

    >>> list_even(3)
    []
    >>> list_even(16)
    [16]
    >>> list_even([1, 2, 3, 4, 5])
    [2, 4]
    >>> list_even([1, 2, [3, 4], 5])
    [2, 4]
    >>> list_even([1, [2, [3, 4]], 5])
    [2, 4]
    """
    ret_list = []
    if not isinstance(obj, list):
        if obj % 2 == 0:
            ret_list.extend([obj])
    else:
        ret_list.extend(
            [list_even(subobj) for subobj in obj]
            )
        ret_list = gather_lists(ret_list)
    return ret_list


def list_odd(obj: Union[list, int]) -> List[int]:
    """
    Return a list of all even integers in obj,
    or sublists of obj, if obj is a list.  If obj is an even
    integer, return a list containing obj.  Otherwise return
    en empty list.

    >>> list_odd(3)
    [3]
    >>> list_odd(16)
    []
    >>> list_odd([1, 2, 3, 4, 5])
    [1, 3, 5]
    >>> list_odd([1, 2, [3, 4], 5])
    [1, 3, 5]
    >>> list_odd([1, [2, [3, 4]], 5])
    [1, 3, 5]
    """
    ret_list = []
    if not isinstance(obj, list):
        if obj % 2 == 1:
            ret_list.extend([obj])
    else:
        ret_list.extend(
            [list_odd(subobj) for subobj in obj]
            )
        ret_list = gather_lists(ret_list)
    return ret_list
    

def count_even(obj: Union[list, int]) -> int:
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    >>> count_even(3)
    0
    >>> count_even(16)
    1
    >>> count_even([1, 2, [3, 4], 5])
    2
    """
    count = 0
    if not isinstance(obj, list):
        return int(obj % 2 == 0)
    else:
        count += sum(
            [count_even(sublist) for sublist in obj]
            )
    return count
    

def count_odd(obj: Union[list, int]) -> int:
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    >>> count_odd(3)
    1
    >>> count_odd(16)
    0
    >>> count_odd([1, 2, [3, 4], 5])
    3
    """
    count = 0
    if not isinstance(obj, list):
        return int(obj % 2 == 1)
    else:
        count += sum(
            [count_odd(sublist) for sublist in obj]
            )
    return count


def count_all(obj: Union[list, object]) -> int:
    """
    Return the number of elements in obj or sublists of obj if obj is a list.
    Otherwise, if obj is a non-list return 1.

    >>> count_all(17)
    1
    >>> count_all([17, 17, 5])
    3
    >>> count_all([17, [17, 5], 3])
    4
    """
    count = 0
    if not isinstance(obj, list):
        return 1
    else:
        count += sum(
            [count_all(subobj) for subobj in obj]
            )
    return count


def count_above(obj: Union[list, int], n: int) -> int:
    """
    Return tally of numbers in obj, and sublists of obj, that are over n, if
    obj is a list.  Otherwise, if obj is a number over n, return 1.  Otherwise
    return 0.

    >>> count_above(17, 19)
    0
    >>> count_above(19, 17)
    1
    >>> count_above([17, 18, 19, 20], 18)
    2
    >>> count_above([17, 18, [19, 20]], 18)
    2
    """
    #  Accoring to DocStringExample, the above is strict.
    count = 0
    if not isinstance(obj, list):
        count += int(obj > n)
    else:
        count += sum(
            [count_above(subobj, n) for subobj in obj]
            )
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()