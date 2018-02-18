""""example of top-down programming"""
from typing import List
# grid to check
GRID = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
# an example of a digit_set for testing
DIGIT_SET = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def valid_sudoku(grid: List[List[int]], digit_set: set) -> bool:
    """
    Return whether grid represents a valid,
    complete sudoku.

    Assume grid is square (as many rows as columns)
    and has the same number of rows as elements of
    digit_set.

    >>> valid_sudoku(GRID, DIGIT_SET)
    True
    >>> g = [[x for x in row] for row in GRID]
    >>> g[0][1] = 5
    >>> valid_sudoku(g, DIGIT_SET)
    False
    """
    # let the thoughtful wishing begin
    assert all(len(s) == len(grid) for s in grid)
    assert len(grid) == len(digit_set)
    assert round(len(grid) ** .5) ** 2 == len(grid)

    return (_all_rows_valid(grid, digit_set)
            and _all_columns_valid(grid, digit_set)
            and _all_subsquares_valid(grid, digit_set))


def _all_rows_valid(grid: List[List[int]], digit_set: set) -> bool:
    """
    Return whether all rows in grid are valid and complete.

    Assume grid has same number of rows as elements of digit_set
    and grid has same number of columns as rows.

    >>> _all_rows_valid(GRID, DIGIT_SET)
    True
    >>> g = [[x for x in r] for r in GRID]
    >>> g[0][1] = 5
    >>> _all_rows_valid(g, DIGIT_SET)
    False
    """
    # thoughtful wishing
    return all(_list_valid(r, digit_set) for r in grid)


def _list_valid(r: List[int], digit_set: set) -> bool:
    """
    Return whether r contains each element of digit_set exactly
    once.

    Assume r has same number of elements as digit_set.

    >>> _list_valid(GRID[0], DIGIT_SET)
    True
    >>> L = [x for x in GRID[0]]
    >>> L[1] = 5
    >>> _list_valid(L, DIGIT_SET)
    False
    """
    pass


def _all_columns_valid(grid: List[List[int]], digit_set) -> bool:
    """
    Return whether all columns are complete and valid
    with respect to digit_set.

    Assume the size of digit_set is the same as the number of
    rows and columns of grid.

    >>> _all_columns_valid(GRID, DIGIT_SET)
    True
    >>> g = [[x for x in r] for r in GRID]
    >>> g[1][0] = 5
    >>> _all_columns_valid(g, DIGIT_SET)
    False
    """
    # thoughtful wishing
    return all([
        _list_valid(c, digit_set) for c in _columns(grid)
    ])


def _columns(grid: List[List[int]]) -> List[List[int]]:
    """
    Return list of columns in 2D list grid.

    Assume grid is square, i.e. has same number of rows and
    columns.

    >>> G = [[1, 2], [3, 4]]
    >>> _columns(G)
    [[1, 3], [2, 4]]
    """
    return [_column(i, grid) for i in range(len(grid))]


def _column(i: int, grid: List[List[int]]) -> List[int]:
    """
    Return the ith column of 2D list grid

    Assume i is a valid index for a column of grid, and that
    grid has same number of rows and columns.

    >>> G = [[1, 2], [3, 4]]
    >>> _column(1, G)
    [2, 4]
    """
    return [row[i] for row in grid]


def _all_subsquares_valid(grid: List[List[int]], digit_set: set) -> bool:
    """
    Return whether all subsquares in grid are valid with respect
    to digit_set.

    Assume digit_set has same number of elements as there are rows
    and columns in grid.

    >>> _all_subsquares_valid(GRID, DIGIT_SET)
    True
    >>> g = [[x for x in r] for r in GRID]
    >>> g[0][1] = 5
    >>> _all_subsquares_valid(g, DIGIT_SET)
    False
    """
    # more thoughtful wishing
    pass


def _subsquares(grid: List[List[int]]) -> List[List[int]]:
    """
    Return list of subsquares in grid.

    Assume grid has the same number of rows and columns and that
    the subsquares are returned as a list of their elements.

    >>> G = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> _subsquares(G)
    [[1, 2, 5, 6], [3, 4, 7, 8], [9, 10, 13, 14], [11, 12, 15, 16]]
    """
    pass


def _subsquare(i: int, grid: List[List[int]]) -> List[int]:
    """
    Return the list of elements in ith subsquare of grid.

    Assume grid has the same number, n, of rows and columns and
    that n is a perfect square, and i is a valid index for grid.

    >>> G = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> _subsquare(2, G)
    [9, 10, 13, 14]
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
