"""
The Bag class represents a bag (or multiset) of generic items. It supports insertion and iterating over the
items in arbitrary order.

This implementation uses a singly linked list with a static nested class Node.
See {@link LinkedBag} for the version from the textbook that uses a non-static nested class.
See {@link ResizingArrayBag} for a version that uses a resizing array.

The <em>add</em>, <em>isEmpty</em>, and <em>size</em> operations take constant time. Iteration takes time proportional
to the number of items.

For additional documentation, see <a href="https://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
"""


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0
        self.nodes = []

    def isEmpty(self):
        """Returns true if this bag is empty.

        :return: True if bag is empty, False otherwise.
        """
        return self.first is None

    def size(self):
        """Returns the number of items in this bag.

        :return: the number of items in this bag
        """
        return self.n

    def add(self, item):
        self.nodes.append(item)

    def __iter__(self):
        yield self.nodes[self.n]

    def __next__(self):
        if self.isEmpty():
            raise StopIteration("Empty Container")
        for n in self.nodes:
            return n


if __name__ == '__main__':
    bag = Bag()
    print(bag.isEmpty())
    print(bag.size())
    bags = list(bag)
    for bag in bags:
        print(bag)

