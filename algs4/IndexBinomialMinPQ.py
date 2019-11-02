"""
The IndexBinomialMinPQ class represents an indexed priority queue of generic keys.
It supports the usual insert and delete-the-minimum operations,
long with delete and change-the-key methods.
In order to let the client refer to keys on the priority queue,
an integer between 0 and N-1 is associated with each key ; the client
uses this integer to specify which key to delete or change.
It also supports methods for peeking at the minimum key,
testing if the priority queue is empty, and iterating through
 the keys.

This implementation uses a binomial heap along with an array to associate
 keys with integers in the given range.
he insert, delete-the-minimum, delete, change-key, decrease-key,
increase-key and size operations take logarithmic time.
The is-empty, min-index, min-key, and key-of operations take constant time.
Construction takes time proportional to the specified capacity.

Java version @author Tristan Claverie
"""


class ArithmeticException(Exception):
    pass


class IllegalArgumentException(Exception):
    pass


class Node:
    def __init__(self):
        pass


class Key:
    def __init__(self):
        pass


class IndexBinomialMinPQ:
    def __init__(self, N):
        if N < 0:
            raise IllegalArgumentException("Cannot create a priority queue of negative size.")
        self.n = N
        self.key = None
        self.order = None
        self.index = None
        self.parent = None
        self.child = None
        self.sibling = None
        self.head = None
        self.nodes = [None] * self.n

    def isEmpty(self):
        """Whether the priority queue is empty. Worst case is O(1).

        :return: True if the priority queue is empty, False otherwise.
        """
        if self.head is None:
            return True

    def contains(self, i):
        """ Check whether i is in the priority Queue.

        :return: true if i is present. raises Illegal Argument Exception if the i is out of bounds.
        """
        if i < 0 or i > self.n:
            raise IllegalArgumentException()

        else:
            return self.nodes[i] is not None

    def size(self):
        """Number of elements currently on the priority queue.

        Worst case is O(log(n))

        :return: The number of elements on the priority queue.
        """
        result = 0
        node = self.head
        while node is not None:
            if node.order > 30:
                raise ArithmeticException("The number of elements cannnot be evaluated, but the priority queue is still valid.")

            tmp = 1 << node.order
            result = result | tmp
        return result

