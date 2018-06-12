from typing import List

## This is a function that uses same concept
## of quick-sort to produce the kth smallest
## number in a unsorted list of integers.
## You don't have to remember how it's done
## But I hope you understand why it can be done
## this way

def quick_select(L: List[int], k: int):
    """
    Returns the <k>th smallest item in given
    list <L>. If the list does not contain at
    least k elements, the function produce False.

    Pre-condition: No duplicate elements in L

    >>> quick_select([], 5)
    False
    >>> quick_select([3, 1, 2], 4)
    False
    >>> quick_select([2, 1, 4, 3, 5, 7, 6], 1)
    1
    >>> quick_select([2, 1, 4, 3, 5, 7, 6], 5)
    5
    """
    lst = L.copy()
    while len(lst) >= k:
        pivot = lst[0]
        smaller = [n for n in lst if n < pivot]
        greater = [n for n in lst if n > pivot]
        if k <= len(smaller):
            lst = smaller
        elif k == len(smaller) + 1:
            return pivot
        else:
            lst = greater
            k = k - len(smaller) - 1
    return False
