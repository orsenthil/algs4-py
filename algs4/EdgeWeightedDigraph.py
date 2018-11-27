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


class EdgeWeightedDigraph:

    def __init__(self, V=None, E=None, In=None):
        """Initializes an empty edge-weighted digraph with {@code V} vertices and {@code E} edges.

        @throws ValueError if {@code V < 0}
        :param V: the number of vertices.
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
            for v in range(V):
                self.adj[v] = Bag()

        self.E = 0
        self.indegree = []
        self.adj = []
        self.indegree = []

        if In is not None:
            pass



    def addEdge(self, edge):
        """
        Adds the directed edge {@code e} to this edge-weighted digraph.
        @param  e the edge
        @throws IllegalArgumentException unless endpoints of edge are between {@code 0} and {@code V-1}

        :param edge:
        :return:
        """
        v = edge.from()
        w = edge.to()
        validateVertex(v)
        validateVertex(w)
        self.adj[v].add(edge)
        self.indegree[w] += 1
