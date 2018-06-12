# March 19 2018, Lecture 0101

def fib(n: int) -> int:
    """ Return nth fibonacci number

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(3)
    2
    """
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib_mem(n: int, seen: dict) -> int:
    """
    return nth fibonacci number *quickly*
    """
    if n not in seen:
        if n < 2:
            seen[n] = n
        else:
            seen[n] = fib_mem(n - 2, seen) + fib_mem(n - 1, seen)
    return seen[n]