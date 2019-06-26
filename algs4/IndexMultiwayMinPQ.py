"""
An index multiway heap.
"""


class IllegalArgumentException(Exception):
    pass


class IndexMultiwayMinPQ:

    def __init__(self, minN):
        if minN < 0:
            raise IllegalArgumentException()
