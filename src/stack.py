# Python program to demonstrate
# stack implementation using a linked list.
# node class

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = Node("head")
        self.size = 0
    
    # string representation of Stack
    def __str__(self) -> str:
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.val) + "->"
            cur = cur.next
        return out[::-2]

    def getSize(self):
        pass

    def isEmpty(self):
        pass

    def peek(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass