"""
The {@code IndexMinPQ} class represents an indexed priority queue of generic keys.
It supports the usual <em>insert</em> and <em>delete-the-minimum</em>
operations, along with <em>delete</em> and <em>change-the-key</em>
methods. In order to let the client refer to keys on the priority queue,
an integer between {@code 0} and {@code maxN - 1}
is associated with each key—the client uses this integer to specify
which key to delete or change.
It also supports methods for peeking at the minimum key,
testing if the priority queue is empty, and iterating through
the keys.
<p>
This implementation uses a binary heap along with an array to associate
keys with integers in the given range.
The <em>insert</em>, <em>delete-the-minimum</em>, <em>delete</em>,
<em>change-key</em>, <em>decrease-key</em>, and <em>increase-key</em>
operations take logarithmic time.
The <em>is-empty</em>, <em>size</em>, <em>min-index</em>, <em>min-key</em>,
<em>contains</em>, and <em>key-of</em> operations take constant time.
Construction takes time proportional to the specified capacity.
<p>
For additional documentation, see <a href="https://algs4.cs.princeton.edu/24pq">Section 2.4</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.

the generic type of key on this priority queue

Reference

* https://algs4.cs.princeton.edu/24pq/
"""


class IllegalArgumentException(Exception):
    pass


class NoSuchElementException(Exception):
    pass


class IndexMinPQ:

    def __init__(self, maxN):
        if maxN < 0:
            raise IllegalArgumentException()
        self.maxN = maxN        # maximum number of elements on PQ.
        self.n = 0              # number of elements on PQ.
        self.pq = []            # binary heap using 1 based indexing
        self.qp = []            # inverse of pq - qp[pq[i]] = pq[qp[i]] = i
        self.keys = []          # keys[i] = priority of i

        for i in range(maxN):
            self.qp.append(-1)

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

    def maxIndex(self):
        """Returns an index associated with a maximum key.

        :return: an index associated with a maximum key.
        throws NoSuchElementException if this priority queue is empty.

        """
        if self.n == 0:
            raise NoSuchElementException("Priority Queue Underflow")

        return self.pq[1]

    # General Helper Functions

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j
