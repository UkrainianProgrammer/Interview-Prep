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
        return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value

    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        removeNode = self.head.next
        self.head.next = removeNode.next
        self.size -= 1
        return removeNode.val

if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        top_value = stack.pop()
        print(f"Pop: {top_value}") # variable name changed
    print(f"Stack: {stack}")