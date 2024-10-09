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

    # return true if the passed node is a leaf node
    def isLeaf(self, pos):
        return pos*2 > self.size

    # swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    
    # heapify the node at pos
    def minHeapify(self, pos):
        # if the node is a non-leaf and greater than any of its 
        # children
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # swap with the left child and heapify
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                
                # swap with the right child and heapify
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
    
    # insert a node into the heap
    def insert(self, node):
        if self.size >= self.maxsize:
            return
        
        self.size += 1
        self.Heap[self.size] = node

        cur = self.size
        # preserve the minHeap structure
        while self.Heap[cur] < self.Heap[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)

    # print the contents
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print("Parent: " + str(self.Heap[i]) + "Left Child: " +
                  str(self.Heap[2 * i]) + "Right Child: " + 
                  str(self.Heap[2 * i + 1]))
