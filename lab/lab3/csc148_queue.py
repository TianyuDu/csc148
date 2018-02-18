"""
queue implementation
"""


class Queue:
    """
    A first-in, first-out (FIFO) queue.
    """

    _container: list

    def __init__(self) -> None:
        """
        Create and initialize new Queue self.

        >>> q = Queue()
        """
        self._container = list()

    def add(self, obj: object) -> None:
        """
        Add object at the back of Queue self.

        >>> q = Queue()
        >>> q.add(7)
        """
        pass

    def remove(self) -> object:
        """
        Remove and return front object from Queue self.

        Queue self must not be empty.

        >>> q = Queue()
        >>> q.add(3)
        >>> q.add(5)
        >>> q.remove()
        3
        """
        pass

    def is_empty(self) -> bool:
        """
        Return whether Queue self is empty

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        >>> q.remove()
        5
        >>> q.is_empty()
        True
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
