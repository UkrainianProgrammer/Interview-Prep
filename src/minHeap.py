# Python implementation of min heap

import sys

class MinHeap:
    def __init__(self, maxsize) -> None:
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    # return the position of
    # parent for the node currently at pos
    def parent(self, pos):
        return pos//2
    
    # return the pos of the left child for
    # node at pos
    def leftChild(self, pos):
        return 2 * pos
    
    # return the pos of the right child for
    # node at pos
    def rightChild(self, pos):
        return (2 * pos) + 1