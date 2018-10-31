"""
The {@code Bag} class represents a bag (or multiset) of
generic items. It supports insertion and iterating over the
items in arbitrary order.
<p>
This implementation uses a singly linked list with a static nested class Node.
See {@link LinkedBag} for the version from the
textbook that uses a non-static nested class.
See {@link ResizingArrayBag} for a version that uses a resizing array.
The <em>add</em>, <em>isEmpty</em>, and <em>size</em> operations
take constant time. Iteration takes time proportional to the number of items.
<p>
For additional documentation, see <a href="https://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
"""
