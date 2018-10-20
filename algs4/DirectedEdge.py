"""
The {@code DirectedEdge} class represents a weighted edge in an
{@link EdgeWeightedDigraph}. Each edge consists of two integers
(naming the two vertices) and a real-value weight. The data type
provides methods for accessing the two endpoints of the directed edge and
the weight.
<p>
For additional documentation, see <a href="https://algs4.cs.princeton.edu/44sp">Section 4.4</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.

@author Robert Sedgewick
@author Kevin Wayne
"""

class DirectedEdge:

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
