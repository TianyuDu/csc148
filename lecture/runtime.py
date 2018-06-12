"""
experiment with run time...
"""
from time import time
from timeit import timeit
from typing import Callable, Any


def silly(n):
    """ a silly function"""
    n = 17 * n ** (1 / 2)
    n += n + 3
    print("n is: {}.".format(n))

    if n > 97:
        print('big!')
    else:
        print('not so big!')


def f1(n):
    """ function example"""
    num = 0
    for i in range(n):
        num += i


def f2(n):
    """ function example"""
    num = 0
    for i in range(n // 2):
        for j in range(n ** 2):
            num += i * j


def f3(n):
    """ function example"""
    i, num = 0, 0
    while i ** 2 < n:
        j = 0
        while j ** 2 < n:
            num += i * j
            j += 1
        i += 1


def f4(n):
    """ function example """
    i, num = 0, 0
    while i < n * n:
        num += i
        i += 1


def f5(n):
    """ function example """
    num = 0
    if n % 2 == 0:
        for i in range(n * n):
            num += 1
    else:
        for i in range(5, n + 3):
            num += i


def f6(n):
    """ function example """
    count = 0
    while n > 1:
        n //= 2
        count += count + 1
    return count


def run_function(f: Callable[[int], Any], test_range: list) -> None:
    """ time a function
    """
    with open("run_data.txt", "w") as data:
        for n in test_range:
            start = time() # start a clock...
            f(n)
            print("Ran {} in {} seconds "
                  "on input size {}".format(f.__name__, time() - start, n))
            # avg_time = timeit("{}({})".format(f.__name__, n), number=10, globals=globals())
            # data.write("{}\t{}\n".format(n, avg_time))
        data.close()


if __name__ == "__main__":
    run_function(f4, [10**i for i in range(6)])
