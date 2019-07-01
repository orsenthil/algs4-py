"""
An index multiway heap.
"""


class IllegalArgumentException(Exception):
    pass


class NoSuchElementException(Exception):
    pass


class IndexMultiwayMinPQ:

    def __init__(self, maxN):
        if maxN < 0:
            raise IllegalArgumentException()

        self.minN = maxN        # maximum number of elements on PQ.
        self.n = 0              # number of elements on PQ.
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
        if i < 0 or i >= self.minN:
            raise IllegalArgumentException("Invalid Values.")
        if self.contains(i):
            raise IllegalArgumentException("index is already in priority queue.")
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swim(self.n)

    # General Helper Functions

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    # Heap Helper Functions

    def swim(self, k):
        while k > 1 and self.greater(k // 2, k):
            self.exch(k, k//2)
            k = k //2