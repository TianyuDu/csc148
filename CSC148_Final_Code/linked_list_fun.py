from typing import Union


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    next_ - successor to this LinkedListNode
    value - data represented by this LinkedListNode
    """

    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None]=None) -> None:
        """
        Create LinkedListNode self with data value and successor next

        >>> LinkedListNode(5).value
        5
        >>> LinkedListNode(5).next_
        """
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        rv = ""
        curr = self
        while curr != None:
            rv += str(curr.value)
            if curr.next_ == None:
                rv += " ->|"
            else:
                rv += " -> "
            curr = curr.next_

        return rv

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        return type(self) == type(other) and \
               self.value == other.value and \
               self.next_ == other.next_


class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: LinkedListNode
    back: LinkedListNode
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front = None
        self.back = None
        self.size = 0

    def __str__(self):
        """
        Return a human-friendly string representation of
        LinkedList self.

        >>> lnk = LinkedList()
        >>> lnk.front = LinkedListNode(5)
        >>> lnk.back = lnk.front
        >>> print(lnk)
        5 ->|
        """
        return str(self.front)

    def __eq__(self, other):
        """
        Return whether LinkedList self is equivalent to
        other.

        @param LinkedList self: this LinkedList
        @param LinkedList|object other: object to compare to self
        @rtype: bool

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        return type(self) == type(other) and \
               self.size == other.size and \
               self.front == other.front and \
               self.back == other.back

    def append(self, value):
        """
        Insert a new LinkedListNode with value after self.back.

        @param LinkedList self: this LinkedList.
        @param object value: value of new LinkedListNode
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        nn = LinkedListNode(value, None)
        if self.front == None:
            self.front = nn
            self.back = nn
            self.size = 1
        else:
            self.back.next_ = nn
            self.back = nn
            self.size += 1

    def prepend(self, value: object) -> None:
        """
        Insert value before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        nn = LinkedListNode(value, None)
        if self.front == None:
            self.front = nn
            self.back = nn
            self.size = 1
        else:
            nn.next_ = self.front
            self.front = nn
            self.size += 1

    def delete_front(self):
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        @param LinkedList self: this LinkedList
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        self.front = self.front.next_
        self.size -= 1

    def __getitem__(self, index):
        """
        Return the value at LinkedList self's position index.

        @param LinkedList self: this LinkedList
        @param int index: position to retrieve value from
        @rtype: object

        >>> lnk = LinkedList()
        >>> lnk.prepend(1)
        >>> lnk.prepend(0)
        >>> lnk.__getitem__(1)
        1
        >>> lnk[-1]
        1
        """
        if index < 0:
            index = self.size + index
        curr = self.front
        while index > 0:
            curr = curr.next_
            index -= 1
        return curr.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.__contains__(1)
        True
        >>> lnk.__contains__(3)
        False
        """
        size = self.size
        curr = self.front
        while size > 0:
            if curr.value == value:
                return True
            curr = curr.next_
            size -= 1
        return False

    # ===========================
    # Implement following methods
    # ===========================

    def repeat_items(self: 'LinkedList') -> None:
        """
        Repeat each item in LinkedList self.
        >>> list1 = LinkedList()
        >>> list1.append(1)
        >>> list1.append(2)
        >>> list1.append(3)
        >>> list1.repeat_items()
        >>> print(list1.front)
        1 -> 1 -> 2 -> 2 -> 3 -> 3 ->|
        """
        pass

    def even_sum(self: 'LinkedList') -> int:
        """
        Produce the sum of all of the even integers.
        >>> list1 = LinkedList()
        >>> list1.append(2)
        >>> list1.append(2)
        >>> list1.append(3)
        >>> list1.even_sum()
        4
        """
        pass


def merge(list1: LinkedList, list2: LinkedList) -> None:
    """
    Merge list1 and list2 by placing list2’s nodes into the
    correct position in list1 to preserve ordering.
    When complete, list1 will contain all the values from both lists, in order, and list2 will be empty.
    Assume list1 and list2 contain comparable values in  non-decreasing order

    >>> list1 = LinkedList()
    >>> list1.append(1)
    >>> list1.append(3)
    >>> list1.append(5)
    >>> list2 = LinkedList()
    >>> list2.append(2)
    >>> list2.append(6)
    >>> merge(list1, list2)
    >>> print(list1.front)
    1 -> 2 -> 3 -> 5 -> 6 ->|
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
