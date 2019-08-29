"""

The IndexFibonacciMinPQ class represents an indexed priority queue of generic keys.

It supports the usual insert and delete-the-minimum operations,
along with delete and change-the-key methods.
In order to let the client refer to keys on the priority queue,
an integer between 0 and N-1 is associated with each key ; the client
uses this integer to specify which key to delete or change.
It also supports methods for peeking at the minimum key,
testing if the priority queue is empty, and iterating through
the keys.

This implementation uses a Fibonacci heap along with an array to associate keys with integers
in the given range.

The insert, size, is-empty, contains, minimum-index, minimum-key and key-of take constant time.
The decrease-key operation takes amortized constant time.

The delete, increase-key, delete-the-minimum, change-key take amortized logarithmic time.
Construction takes time proportional to the specified capacity

@author Tristan Claverie
"""


class IllegalArgumentException(Exception):
    pass


class Node:
    def __init__(self):
        self.node = None
        self.key = None
        self.order = None
        self.index = None
        self.prev = None
        self.next = None
        self.parent = None
        self.child = None
        self.mark = None


class IndexFibonacciMinPQ:

    def __init__(self, N):
        if N < 0:
            raise IllegalArgumentException()

        self.n = N
        self.nodes = []
        self._size = 0

    def size(self):
        """Number of elements currently on the priority queue.

        Worst case is O(1)
        :return: The number of elements on the priority queue.
        """
        return self._size

    def isEmpty(self):
        """Whether the priority queue is empty.

        Worst case is O(1).

        :return: Return if the queue size is 0.
        """
        return self.size() == 0

    def contains(self, i):
        if i < 0 or i > self.n:
            raise IllegalArgumentException()

        return self.nodes[i] is not None