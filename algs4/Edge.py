"""
The {@code Edge} class represents a weighted edge in an
{@link EdgeWeightedGraph}. Each edge consists of two integers
(naming the two vertices) and a real-value weight. The data type
provides methods for accessing the two endpoints of the edge and
the weight. The natural order for this data type is by
ascending order of weight.
<p>
For additional documentation, see <a href="https://algs4.cs.princeton.edu/43mst">Section 4.3</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.

"""


class Edge:

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return "Edge({v}, {w}, {weight})".format(v=self.v, w=self.w, weight=self.weight)

    def weight(self):
        """Returns the weight of the edge.

        :return: The weight of the edge.
        """
        return self.weight


if __name__ == '__main__':
    e = Edge(12, 34, 5.67)
    print(str(e))
