"""
The Edge class represents a weighted edge in an EdgeWeightedGraph. Each edge
consists of two integers (naming the two vertices) and a real-value weight. The
data type provides methods for accessing the two endpoints of the edge and the
weight. The natural order for this data type is by ascending order of weight.
"""


class IllegalArgumentException(Exception):
    pass


class Edge:

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def weight(self):
        """Returns the weight of the edge.

        :return: The weight of the edge.
        """
        return self.weight

    def either(self):
        """Returns either endpoint of this edge.

        :return: either endpoint of this edge.
        """
        return self.v

    def other(self, vertex):
        """Returns the endpoint of this edge that is different from the given
        vertex.

        :param vertex: vertex one endpoint of this edge
        :return: the other endpoint of this edge
        :throws: IllegalArgumentException if the vertex is not one of the
        endpoints of this edge
        """
        if vertex == self.v:
            return self.w
        if vertex == self.w:
            return self.v
        raise IllegalArgumentException("Illegal Endpoint")

    def __eq__(self, other):
        return (self.v, self.w, self.weight) == (other.v,
                                                 other.w,
                                                 other.weight)

    def __ne__(self, other):
        return not (self.v, self.w, self.weight) == (other.v,
                                                     other.w,
                                                     other.weight)

    def __lt__(self, other):
        return (self.v, self.w, self.weight) < (other.v,
                                                other.w,
                                                other.weight)

    def __str__(self):
        return "Edge({v}, {w}, {weight})".format(v=self.v,
                                                 w=self.w,
                                                 weight=self.weight)


if __name__ == '__main__':
    e = Edge(12, 34, 5.67)
    print(str(e))
