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


class EdgeWeightedGraph:

    NEWLINE = "\n"

    def __init__(self, E=None, V=None, In=None, G=None):

        if E is None and V is None and In is None and G is None:
            raise ValueError("One of E, V, In or G argument must be given.")
