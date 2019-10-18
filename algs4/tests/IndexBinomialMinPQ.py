"""
/**
 *  The IndexBinomialMinPQ class represents an indexed priority queue of generic keys.
 *  It supports the usual insert and delete-the-minimum operations,
 *  along with delete and change-the-key methods.
 *  In order to let the client refer to keys on the priority queue,
 *  an integer between 0 and N-1 is associated with each key ; the client
 *  uses this integer to specify which key to delete or change.
 *  It also supports methods for peeking at the minimum key,
 *  testing if the priority queue is empty, and iterating through
 *  the keys.
 *
 *  This implementation uses a binomial heap along with an array to associate
 *  keys with integers in the given range.
 *  The insert, delete-the-minimum, delete, change-key, decrease-key,
 *  increase-key and size operations take logarithmic time.
 *  The is-empty, min-index, min-key, and key-of operations take constant time.
 *  Construction takes time proportional to the specified capacity.
 *
 *  Java version @author Tristan Claverie
 */

"""


class Node:
    def __init__(self):
        pass


class Key:
    def __init__(self):
        pass

class IndexBinomialMinPQ:
    def __init__(self):
        pass