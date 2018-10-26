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
