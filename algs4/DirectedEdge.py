"""

The {@code DirectedEdge} class represents a weighted edge in an {@link
EdgeWeightedDigraph}. Each edge consists of two integers (naming the two
vertices) and a real-value weight. The data type provides methods for accessing
the two endpoints of the directed edge and the weight.

For additional documentation, see <a
href="https://algs4.cs.princeton.edu/44sp">Section 4.4</a> of <i>Algorithms,
4th Edition</i> by Robert Sedgewick and Kevin Wayne.
"""


class DirectedEdge:

    def __init__(self, v, w, weight):
        """
        :param v: The tail vertex
        :param w: The head vertex
        :param weight: The weight of the directed edge.
        """
        self.v = v
        self.w = w
        self.weight = weight

    def from_vertex(self):
        """Returns the tail vertex of the directed edge.

        :return: the tail vertex of the directed edge
        """
        return self.v

    def to_vertex(self):
        """Returns the head vertex of the directed edge.

        :return: the head vertex of the directed edge.
        """
        return self.w

    def __str__(self):
        """Returns a string representation of the directed edge.

        :return: the string representation of the Directed Edge.
        """
        return str(self.v) + "->" + str(self.w) + "  %5.2f" % self.weight


if __name__ == "__main__":
    e = DirectedEdge(12, 34, 5.67)
    print(str(e))
