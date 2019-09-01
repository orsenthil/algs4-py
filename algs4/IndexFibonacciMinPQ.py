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
        self.head = None

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
        """ Returns True if the element i is in the Queue, False otherwise.

        :param i:  Element to test.
        :return: True if the element is present in the Priority Queue, False otherwise.
        """
        if i < 0 or i > self.n:
            raise IllegalArgumentException()

        return self.nodes[i] is not None

    def greater(self, n, m):
        if n == None:
            return False
        if m == None:
            return True

        return n > m


    def insert(self, i, key):
        """ Associates key with index {@code i}.

        :param i:  i is an index.
        :param key:  Key to associate with the index.

        :return: None
        """
        if i < 0 or i >= self.n:
            raise IllegalArgumentException("Invalid Values.")
        if self.contains(i):
            raise IllegalArgumentException("index is already in priority queue.")

        x = Node()
        x.key = key
        x.index = i
        self.nodes[i] = x
        self._size += 1

        head = self.insertNode(x, self.head)

        if self.min == None:
            self.min = head
        else:
            if self.greater(self.min.key, key):
                self.min = head



    """
    //Inserts a Node in a circular list containing head, returns a new head
    private Node<Key> insertNode(Node<Key> x, Node<Key> head) {
        if (head == null) {
            x.prev = x;
        x.next = x;
        } else {
            head.prev.next = x;
        x.next = head;
        x.prev = head.prev;
        head.prev = x;
        }
        return x;
        }
    """

