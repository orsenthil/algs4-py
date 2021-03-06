"""
An index multiway heap.

The IndexMultiwayMinPQ class represents an indexed priority queue of generic keys.

It supports the usual insert and delete-the-minimum operations,
along with delete and change-the-key methods.

In order to let the client refer to keys on the priority queue,
an integer between 0 and N-1 is associated with each key, the client
uses this integer to specify which key to delete or change.

It also supports methods for peeking at the minimum key,
testing if the priority queue is empty, and iterating through
the keys.

This implementation uses a multiway heap along with an array to associate
keys with integers in the given range.

For simplified notations, logarithm in base d will be referred as log-d
The delete-the-minimum, delete, change-key and increase-key operations
take time proportional to d*log-d(n)

The insert and decrease-key take time proportional to log-d(n).

The is-empty, min-index, min-key, size, contains and key-of operations take constant time.
Construction takes time proportional to the specified capacity.

The arrays used in this structure have the first d indices empty, it apparently helps with caching effects.

Credits: algs4 (java version) author Tristan Claverie
"""


class IllegalArgumentException(Exception):
    pass


class NoSuchElementException(Exception):
    pass


class UnsupportedOperationException(Exception):
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
        """ Is i an index on this priority queue?

            :param i: i an idex.
            :return: True if i is an index on this priority queue; False otherwise.
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

    def delMin(self):
        """Removes a minimum key and returns its associated index.

        :return: an index associated with a minimum key
        """
        if self.n == 0:
            raise NoSuchElementException("Priority Queue Underflow")

        min = self.pq[1]
        self.exch(1, self.n - 1)
        self.sink(1)
        self.qp[min] = -1
        self.keys[min] = None
        self.pq[self.n] = -1
        return min

    def keyOf(self, i):
        """ Returns the key associated with index {@code i}.

        :param i: The index of the key to return.

        :return:  The key associated with the index.
        """
        if i < 0 or i > self.minN:
            raise IllegalArgumentException("Illegal Argument given to KeyOf")

        if not self.contains(i):
            raise NoSuchElementException("index is not in the priority queue.")
        else:
            return self.keys[i]

    def changeKey(self, i, key):
        """Change the key associated with index {@code i} to the specified value.

        :param i: The index of the key to change.
        :param key: the key associated with the index i to this key.

        :return: None
        """
        if i < 0 or i >= self.minN:
            raise IllegalArgumentException()

        if not self.contains(i):
            raise NoSuchElementException("Index is not in the priority queue.")

        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def decreaseKey(self, i, key):
        """Decrease the key associated with index {@code i} to the specified value.

        :param i: The index of the key to decrease.
        :param key:  decrease the key associated with the index (i) to this key.

        * @throws IllegalArgumentException unless {@code 0 <= i < maxN}
        * @throws IllegalArgumentException if {@code key >= keyOf(i)}
        * @throws NoSuchElementException no key is associated with index {@code i}

        :return: None
        """
        if i < 0 or i >= self.minN:
            raise IllegalArgumentException()
        if self.contains(i):
            raise NoSuchElementException("index is not in the priority queue.")

        if (self.keys[i] < key):
            raise IllegalArgumentException("Calling decreaseKey() with given argument would not strictly decrease the key")

        self.keys[i] = key
        self.swim(self.qp[i])

    def increaseKey(self, i, key):
        """ Increase the key associated with index {@code i} to the specified value.

        :param i: The index of the key to increase.
        :param key: Increase the key associated with the index to this key.

        * @throws IllegalArgumentException unless {@code 0 <= i < maxN}
        * @throws IllegalArgumentException if {@code key <= keyOf(i)}
        * @throws NoSuchElementException no key is associated with index {@code i}

        :return: None
        """
        if i < 0 or i >= self.minN:
            raise IllegalArgumentException()

        if not self.contains(i):
            raise NoSuchElementException("index is not in the priority queue.")

        if self.keys[i] > key:
            raise IllegalArgumentException("Calling increaseKey() with given argument would not strictly increase the key")

        self.keys[i] = key
        self.sink(self.qp[i])

    def delete(self, i):
        """ Remove the key associated with index {@code i}.

        :param i:  The index of the key to remove.

        * @throws IllegalArgumentException unless {@code 0 <= i < maxN}
        * @throws NoSuchElementException no key is associated with index {@code i}
        :return: None
        """
        if i < 0 or i >= self.minN:
            raise IllegalArgumentException()

        if not self.contains(i):
            raise NoSuchElementException("index is not in the priority queue.")

        index = self.qp[i]

        self.exch(index, self.n)
        self.n -=1
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1

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

    def sink(self, k):
        while (2 * k <= self.n):
            j = 2 * k
            if j < self.n and self.greater(j, j + 1):
                j = j + 1
            if not self.greater(k, j):
                break
            self.exch(k, j)
            k = j

    def hasNext(self):
        assert isinstance(self.copy, IndexMultiwayMinPQ)
        return not self.copy.isEmpty()

    def remove(self):
        raise UnsupportedOperationException()

    def __iter__(self):
        yield self.copy.delMin()

    def __next__(self):
        if not self.hasNext():
            raise NoSuchElementException()


if __name__ == '__main__':
    strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"]

    pq = IndexMultiwayMinPQ(len(strings))

    for idx in range(len(strings)):
        pq.insert(idx, strings[idx])

    while not pq.isEmpty():
        i = pq.delMin()
        print(i, strings[i])
    print()

    # reinsert the same strings.
    for idx in range(len(strings)):
        pq.insert(idx, strings[idx])

    # print each key using the iterator
    for i in pq:
        print(i, strings[i])

    # empty the queue.
    while not pq.isEmpty():
        pq.delMin()
