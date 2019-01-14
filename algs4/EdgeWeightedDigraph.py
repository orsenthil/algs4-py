"""
The {@code EdgeWeightedDigraph} class represents a edge-weighted
digraph of vertices named 0 through <em>V</em> - 1, where each
directed edge is of type {@link DirectedEdge} and has a real-valued weight.
It supports the following two primary operations: add a directed edge
to the digraph and iterate over all of edges incident from a given vertex.
It also provides
methods for returning the number of vertices <em>V</em> and the number
of edges <em>E</em>. Parallel edges and self-loops are permitted.
<p>

This implementation uses an adjacency-lists representation, which
is a vertex-indexed array of {@link Bag} objects.
All operations take constant time (in the worst case) except
iterating over the edges incident from a given vertex, which takes
time proportional to the number of such edges.
<p>

For additional documentation,
see <a href="https://algs4.cs.princeton.edu/44sp">Section 4.4</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
"""

import random

from Bag import Bag
from DirectedEdge import DirectedEdge


class EdgeWeightedDigraph:

    def __init__(self, V=None, E=None, In=None):
        """Initializes an empty edge-weighted digraph with {@code V} vertices and {@code E} edges.

        @throws ValueError if {@code V < 0}
        :param V: the number of vertices.
        :param E: the number of edges.
        """
        if V is not None and V < 0:
            raise ValueError("Number of vertices in a Digraph must be nonnegative.")

        if E is not None and E < 0:
            raise ValueError("Number of Edges in a Digraph must be nonnegative.")

        if E is None and V is None and In is None:
            raise ValueError("Invalid ")

        if V is not None and E is None:
            for v in range(V):
                self.adj[v] = Bag()

        if V is not None and E is not None:
            self.V = V
            for v in range(V):
                self.adj[v] = Bag()
            for e in range(E):
                v1 = random.choice(range(self.V))
                v2 = random.choice(range(self.V))
                w = random.randint() * 100
                self.addEdge(DirectedEdge(v1, v2, w))

        self.E = 0

        self.indegree = []
        self.adj = []

        if In is not None:
            pass

    def addEdge(self, edge: DirectedEdge):
        """
        Adds the directed edge {@code e} to this edge-weighted digraph.

        throw ValueError unless endpoints of edge are between {@code 0} and {@code V-1}

        :param edge: Edge of the Digraph.
        :return: None
        """
        v = edge.from_vertex()
        w = edge.to_vertex()

        self.validateVertex(v)
        self.validateVertex(w)

        self.adj[v].add(edge)
        self.indegree[w] += 1

    def validateVertex(self, v):
        """ Validate the value of the vertex  v.

        :param v: vertex to validate
        :return: True for a valid version, or raise a ValueError
        """
        if v < 0 or v > self.V:
            raise ValueError("Vertex {v} cannot be less than 0 or greater than V")

        return True

    def vertices(self):
        """Returns the number of vertices in this edge-weighted digraph.
        """
        return self.V

    def V(self):
        """Returns the vertices in this edge weighted digraph.
        """
        return self.V

    def E(self):
        """Returns the number of edges in this edge-weighted digraph.
        """
        return self.edges()

    def adjV(self, v):
        """Returns the directed edges incident from vertex {@code v}.
        @param  v the vertex
        @return the directed edges incident from vertex {@code v} as an Iterable
        @throws IllegalArgumentException unless {@code 0 <= v < V}

        :return:
        """
        self.validateVertex(v)
        return self.adj[v]

    def outDegree(self, v):
        """Returns the number of directed edges incident from vertex {@code v}.
          This is known as the <em>outdegree</em> of vertex {@code v}.

        :param v:  The vertex
        :return:  The outdegree of vertex v
        @throws IllegalArgumentException unless {@code 0 <= v < V}
        """
        self.validateVertex(v)
        return len(self.adj[v])

    def inDegree(self, v):
        """Returns the number of directed edges incident to vertex {@code v}.
        This is known as the <em>indegree</em> of vertex {@code v}.
        @param  v the vertex
        @return the indegree of vertex {@code v}
        @throws IllegalArgumentException unless {@code 0 <= v < V}

        :param v: The vertex v
        :return:
        """
        self.validateVertex(v)
        return self.indegree[v]

    def edges(self):
        """
        Returns all directed edges in this edge-weighted digraph.
        To iterate over the edges in this edge-weighted digraph, use foreach notation:
        {@code for (DirectedEdge e : G.edges())}.
        @return all edges in this edge-weighted digraph, as an iterable.
        """
        l = []
        for v in range(self.vertices()):
            l.append(self.adj[v])
        return l

    def __str__(self):
        """Returns a string representation of this edge-weighted digraph.

        @return: the number of vertices <em>V</em>, followed by the number of edges <em>E</em>,
        followed by the <em>V</em> adjacency lists of edges
        """
        return "EdgedWeightedDigraph (V={V}, E={E}".format(V=self.V, E=self.E)


if __name__ == '__main__':
    ewd = EdgeWeightedDigraph(10)
    print(ewd.V())
    print(ewd.edges())
