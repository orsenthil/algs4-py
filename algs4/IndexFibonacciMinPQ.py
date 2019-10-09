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

import copy


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


class UnsupportedOperationException(Exception):
    pass


class NoSuchElementException(Exception):
    pass


class IndexFibonacciMinPQ:

    def __init__(self, N):
        if N < 0:
            raise IllegalArgumentException()

        self.n = N
        self.nodes = []
        self._size = 0
        self.head = None
        self.copyitem = None
        self.min = None
        self.table = dict()

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
        if n is None:
            return False
        if m is None:
            return True

        return n > m

    def delMin(self):
        if self.n == 0:
            raise NoSuchElementException("Priority Queue Underflow")
        
        head = self.cut(self.min, self.head)
        x = self.min.child
        index = self.min.index
        self.min.key = None
        if x is not None:
            x.parent = None
            x = x.next

            while x != self.min.child:
                x.parent = None
                x = x.next

            head = self.meld(head, x)

        self._size -= 1
        if (self.isEmpty()):
            self.consolidate()
        else:
            self.min = None
        self.nodes[index] = None
        return index

    def keyOf(self, i):
        if i < 0 or i >= self.n:
            raise IllegalArgumentException

        if not self.contains(i):
            raise NoSuchElementException("Specified index is not in the Queue.")

        return self.nodes[i].key

    def changeKey(self, i, key):
        if i < 0 or i >= self.n:
            raise IllegalArgumentException()

        if not self.contains(i):
            raise NoSuchElementException("Specified index is not in the queue.")

        if self.greater(key, self.nodes[i].key):
            self.increaseKey(i, key)
        else:
            self.decreaseKey(i, key)


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

        if self.min is None:
            self.min = head
        else:
            if self.greater(self.min.key, key):
                self.min = head

    def insertNode(self, x, head):
        if head is None:
            x.prev = x
            x.next = x
        else:
            head.prev.next = x
            x.next = head
            x.prev = head.prev
            head.prev = x

        return x

    def cut(self, x, head=None):
        if x.head == x:
            x.next = None
            x.prev = None
            return None
        else:
            x.next.prev = x.prev
            x.prev.next = x.next
            res = x.next
            x.next = None
            x.prev = None
            if head == x:
                return res
            else:
                return head

    def meld(self, x, y):
        if x is None:
            return y
        if y is None:
            return x
        x.prev.next = y.next
        y.next.prev = x.prev
        x.prev = y
        y.next = x
        return x

    def hasNext(self):
        assert isinstance(self.copyitem, IndexFibonacciMinPQ)
        return not self.copyitem.isEmpty()

    def __iter__(self):
        self.copyitem = copy.deepcopy(self)
        yield self.copyitem

    def __next__(self):
        if self.copyitem.isEmpty():
            raise UnsupportedOperationException
        self.copyitem.delMin()
        pass

    def __del__(self):
        raise UnsupportedOperationException

    def consolidate(self):
        """Coalesces the roots, thus reshapes the heap.
        Caching a HashMap improves greatly performances

        :return:

        		table.clear();
		Node<Key> x = head;
		int maxOrder = 0;
		min = head;
		Node<Key> y = null, z = null;
		do {
			y = x;
			x = x.next;
			z = table.get(y.order);
			while (z != null) {
				table.remove(y.order);
				if (greater(y.key, z.key)) {
					link(y, z);
					y = z;
				} else {
					link(z, y);
				}
				z = table.get(y.order);
			}
			table.put(y.order, y);
			if (y.order > maxOrder) maxOrder = y.order;
		} while (x != head);
		head = null;
		for (Node<Key> n : table.values()) {
			min = greater(min.key, n.key) ? n : min;
			head = insert(n, head);
		}
	}
        """
        self.table.clear()
        x = self.head
        maxOrder = 0
        min = self.head
        y = None
        z = None
        y = x
        x = x.next
        z = self.table.get(y.order)

        while z is not None:
            del self.table[y.order]
            if (self.greater(y.key, z.key)):
                self.link(y, z)
                y = z
            else:
                self.link(z, y)

            z = self.table.get(y.order)

        self.table.put(y.order, y)

        if y.order > maxOrder:
            maxOrder = y.order

        while x != self.head:
            y = x
            x = x.next
            z = self.table.get(y.order)

            while z is not None:
                self.table.remove(y.order)
                if (self.greater(y.key, z.key)):
                    self.link(y, z)
                    y = z
                else:
                    self.link(z, y)

                z = self.table.get(y.order)

            self.table.put(y.order, y)

            if y.order > maxOrder:
                maxOrder = y.order

        self.head = None
        for n in self.table.values():
            if n:
                min = self.greater(min.key, n.key)

            head = self.insert(n, self.head)


    def increaseKey(self, i, key):
        """Insert the key at i.

        :param i: location in the PQ.
        :param key:  Key value
        """
        if i < 0 or i >= self.n:
            raise IllegalArgumentException
        
        if not self.contains(i):
            raise NoSuchElementException("Specified index is not in the queue.")
        
        if self.greater(self.nodes[i].key, key):
            raise IllegalArgumentException("Calling with this argument would not increase the key.")
        
        self.delete(i)
        self.insert(i, key)

    def decreaseKey(self, i, key):
        """Delete the key at i.

        :param i: location in the PQ.
        :param key:  Key value
        """
        if i < 0 or i >= self.n:
            raise IllegalArgumentException

        if not self.contains(i):
            raise NoSuchElementException("Specified index is not in the queue.")

        if self.greater(self.nodes[i].key, key):
            raise IllegalArgumentException("Calling with this argument would not increase the key.")

        x = self.nodes[i]

        if self.greater(self.min.key, key):
            self.min = x

        if x.parent != None and self.greater(x.parent.key, key):
            self.cut(i)

    def delete(self, i):
        """Delete an Element from the Queue.

        :param i: The element to delete.
        """
        if i < 0 or i >= self.n:
            raise IllegalArgumentException()

        if not self.contains(i):
            raise NoSuchElementException("Specified Index is not in the queue.")

        x = self.nodes[i]
        x.key = None

        if x.parent is not None:
            self.cut(i)

        if x.child is not None:
            child = x.child
            x.child = None
            x = child

            child.parent = None
            child = child.next

            while child != x:
                child.parent = None
                child = child.next

            self.head = self.meld(self.head, child)

        if not self.isEmpty():
            self.consolidate()
        else:
            self.min = None

        self.nodes[i]= None
        self.size -= 1

    def link(self, y, z):
        pass

