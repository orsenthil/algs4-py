"""
The {@code EdgeWeightedGraph} class represents an edge-weighted
graph of vertices named 0 through <em>V</em> – 1, where each
undirected edge is of type {@link Edge} and has a real-valued weight.
It supports the following two primary operations: add an edge to the graph,
iterate over all of the edges incident to a vertex. It also provides
methods for returning the number of vertices <em>V</em> and the number
of edges <em>E</em>. Parallel edges and self-loops are permitted.
By convention, a self-loop <em>v</em>-<em>v</em> appears in the
adjacency list of <em>v</em> twice and contributes two to the degree
of <em>v</em>.
<p>

This implementation uses an adjacency-lists representation, which
is a vertex-indexed array of {@link Bag} objects.
All operations take constant time (in the worst case) except
iterating over the edges incident to a given vertex, which takes
time proportional to the number of such edges.
<p>
For additional documentation,
see <a href="https://algs4.cs.princeton.edu/43mst">Section 4.3</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
"""
import DirectedEdge
from Bag import Bag


class IllegalArgumentException(Exception):
    pass


class EdgeWeightedGraph:

    NEWLINE = "\n"

    def __init__(self, E=None, V=None, In=None, G=None):

        self.G = None
        self.E = None
        self.adj = []
        self.indegree = []

        if E is None and V is None and In is None and G is None:
            raise ValueError("One of E, V, In or G argument must be given.")

        if V is not None:
            if V < 0:
                raise IllegalArgumentException("Number of vertices must be non-negative.")
            self.V = V
            self.E = 0
            for v in range(self.V):
                self.adj.append(Bag())

        if E is not None:
            if E < 0:
                raise IllegalArgumentException("Number of Edges must be non-negative.")
            self.E = E

        if In is not None:
            E = In.readInt()
            if E < 0:
                raise IllegalArgumentException("Number of Edges must be non-negative.")

        if G is not None:
            self.G = G
            self.V = G.V()

    def vertices(self):
        """Returns the number of vertices in this edge-weighted digraph.
        """
        return self.V

    def V(self):
        """Returns the number of vertices in this edge-weighted graph.

        :return: The number of vertices in this edge weighted graph.
        """
        return self.V

    def E(self):
        """Returns the number of edges in this edge-weighted graph.

        :return:  The number of edges in this edge weighted graph.
        """
        return self.E

    def validateVertex(self, v):
        """ Validate the value of the vertex  v.

        :param v: vertex to validate
        :return: True for a valid version, or raise a ValueError
        """
        if v < 0 or v > self.V:
            raise ValueError("Vertex {v} cannot be less than 0 or greater than V")

        return True

    def adj(self, v):
        """Returns the edges incident on vertex {@code v}.

        @param  v the vertex
        @return the edges incident on vertex {@code v} as an Iterable
        @throws IllegalArgumentException unless {@code 0 <= v < V}

        :return: the edges incident on vertex {@code v} as an Iterable
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

    def addEdge(self, edge: DirectedEdge):
        """
        Adds the directed edge {@code e} to this edge-weighted graph.
        The edges are added between vertices in both directions.

        throw ValueError unless endpoints of edge are between {@code 0} and {@code V-1}

        :param edge: Edge of the EdgeWeightedGraph.
        :return: None
        """
        v = edge.from_vertex()
        w = edge.to_vertex()

        self.validateVertex(v)
        self.validateVertex(w)

        self.adj[v].add(edge)
        self.adj[w].add(edge)
        self.indegree[w] += 1
        self.indegree[v] += 1
        self.E += 1

    def __str__(self):
        """Returns a string representation of this edge-weighted graph.

        @return: the number of vertices <em>V</em>, followed by the number of edges <em>E</em>,
        followed by the <em>V</em> adjacency lists of edges
        """
        return "EdgedWeightedGraph (V={V}, E={E}".format(V=self.V, E=self.E)


if __name__ == '__main__':
    ewd = EdgeWeightedGraph(10)
    print(ewd.V())
    print(ewd.E)
    print(ewd.edges())
