"""
A generic queue, implemented using a linked list.

% python Queue.py tobe.txt
to be or not to be (2 left on queue)

"""


class NoSuchElementException(ValueError):
    pass


class Node:
    def __init__(self):
        self.item = None
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def isEmpty(self):
        """Returns true if this queue is empty.

        :return: True if the queue is empty, False otherwise
        """
        return self.first is None

    def size(self):
        """Return the number of items in this queue.

        :return: n the number of items in this queue.
        """
        return self.n


    def peek(self):
        """Returns the item least recently added to this queue.

        :return: The item least recently added to the queue.
        """
        if self.isEmpty():
            raise NoSuchElementException("Queue underflow.")

        return self.first.item

    def enqueue(self, item):
        """ Adds the item to this queue.

        :param item:  Item to add to the queue.
        :return: None
        """
        oldlast = self.last
        self.last = Node()
        self.last.item = item
        self.last.next = None

        if self.isEmpty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.n += 1
