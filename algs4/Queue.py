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

    def __str__(self):
        return str(self.item)


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.itern = 0
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
        """Adds the item to this queue.

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

    def dequeue(self):
        """Removes and returns the item on this queue that was least recently added.

        :return: the item on this queue that was least recently added
        """

        if self.isEmpty():
            raise NoSuchElementException("Queue underflow.")

        item = self.first.item
        self.first = self.first.next

        self.n -= 1

        if self.isEmpty():
            self.last = None

        return item

    def __iter__(self):
        self.itern = self.n
        return self


    def __next__(self):
        if self.isEmpty():
            raise StopIteration("Queue underflow.")

        item = self.first.item
        self.first = self.first.next

        self.itern -= 1

        if self.isEmpty():
            self.last = None

        return item

    def __str__(self):
        return str(self.first)


if __name__ == '__main__':
    n1 = Node()
    n1.item = "item1"
    n2 = Node()
    n2.item = "item2"
    q = Queue()
    q.enqueue(n1)
    q.enqueue(n2)
    for q1 in iter(q):
        print(q1)
    q.dequeue()
    for q1 in iter(q):
        print(q1)
