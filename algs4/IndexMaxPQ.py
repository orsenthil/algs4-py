"""
The {@code IndexMaxPQ} class represents an indexed priority queue of generic keys.
It supports the usual <em>insert</em> and <em>delete-the-maximum</em>
operations, along with <em>delete</em> and <em>change-the-key</em>
methods. In order to let the client refer to items on the priority queue,
an integer between {@code 0} and {@code maxN - 1}
is associated with each key—the client
uses this integer to specify which key to delete or change.

It also supports methods for peeking at a maximum key,
testing if the priority queue is empty, and iterating through
the keys.
<p>

This implementation uses a binary heap along with an array to associate
keys with integers in the given range.
The <em>insert</em>, <em>delete-the-maximum</em>, <em>delete</em>,
<em>change-key</em>, <em>decrease-key</em>, and <em>increase-key</em>
operations take logarithmic time.

The <em>is-empty</em>, <em>size</em>, <em>max-index</em>, <em>max-key</em>,
<em>contains</em>, and <em>key-of</em> operations take constant time.
Construction takes time proportional to the specified capacity.
"""


class IllegalArgumentException(Exception):
    pass


class NoSuchElementException(Exception):
    pass


class UnsupportedOperationException(Exception):
    pass


class IndexMaxPQ:

    def __init__(self, maxN):
        if maxN < 0:
            raise IllegalArgumentException()

        self.maxN = maxN    # maximum number of elements in the priority queue.
        self.n = 0          # number of elements in the priority Queue.
        self.pq = []            # binary heap using 1 based indexing
        self.qp = []            # inverse of pq - qp[pq[i]] = pq[qp[i]] = i
        self.keys = []          # keys[i] = priority of i

        for i in range(maxN):
            self.qp.append(-1)

        self.copy = None

    def isEmpty(self):
        """Return True if the PQ is Empty.

        :return:  True if the PR is empty, False otherwise.
        """
        if self.n == 0:
            return True

        return False

    def contains(self, i):
        """ Is {@code i} an index on this priority queue?

        :param i: i an idex.

        :return: @return {@code true} if {@code i} is an index on this priority queue; {@code false} otherwise
        """
        return self.qp[i] != -1

    def size(self):
        """ Returns the number of keys on this priority queue.

        :return: The number of keys on this priority queue.
        """
        return self.n

    def insert(self, i, key):
        """ Associates key with index {@code i}.

        :param i:  i is an index.
        :param key:  Key to associate with the index.

        :return: None
        """
        if i < 0 or i >= self.maxN:
            raise IllegalArgumentException("Invalid Values.")
        if self.contains(i):
            raise IllegalArgumentException("index is already in priority queue.")
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swim(self.n)

    def maxIndex(self):
        """Returns an index associated with a maximum key.

        :return: an index associated with a maximum key.
        throws NoSuchElementException if this priority queue is empty.

        """
        if self.n == 0:
            raise NoSuchElementException("Priority Queue Underflow")

        return self.pq[1]

    def minKey(self):
        """Returns a minimum key.

        :return: a minimum key
        """
        if self.n == 0:
            raise NoSuchElementException("Priority Queue Underflow")
        return self.keys[self.pq[1]]
