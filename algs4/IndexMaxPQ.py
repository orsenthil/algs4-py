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
