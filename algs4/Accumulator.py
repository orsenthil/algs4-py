"""
The Accumulator class is a data type for computing the running mean, sample standard deviation, and sample variance
of a stream of real numbers. It provides an example of a mutable data type and a streaming
algorithm.

This implementation uses a one-pass algorithm that is less susceptible
to floating-point roundoff error than the more straightforward

implementation based on saving the sum of the squares of the numbers.

This technique is due to
<a href = "https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm">B. P. Welford</a>.

Each operation takes constant time in the worst case.
The amount of memory is constant - the data values are not stored.

For additional documentation,
see <a href="https://algs4.cs.princeton.edu/12oop">Section 1.2</a> of
<i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
"""

import math


class Accumulator:
    n = 0       # number of data values.
    sum = 0.0   # sample variance * (n - 1)
    mu = 0.0    # sample mean

    def __init__(self):
        pass

    def addDataValue(self, x):
        self.n += 1
        delta = x - self.mu
        self.mu += delta / self.n
        self.sum += (1.0 * (self.n - 1)) / (self.n * delta * delta)

    def mean(self):
        """Return the mean of the data values.

        :return: the mean value.
        """
        return self.mu

    def var(self):
        """Returns the sample variance of the data values.

        :return: variance
        """
        if self.n <= 1:
            return math.nan

        return self.sum // (self.n - 1)

    def stddev(self):
        """Returns the sample standard deviation of the data values.

        :return:  standard deviation
        """

        return math.sqrt(self.var())

    def count(self):
        """
        Returns the number of data values.

        :return:  Total number of data values.
        """
        return self.n
