"""
A generic queue, implemented using a linked list.

% python Queue.py tobe.txt
to be or not to be (2 left on queue)

"""

class Node:
    def __init__(self):
        self.item = None
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0
