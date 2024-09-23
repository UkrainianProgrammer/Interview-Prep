# Implementation of Queue class using two stacks with expensive dequeue()

class Queue:
    def __init__(self) -> None:
        self.stackIn = []
        self.stackOut = []
    
    def enqueue(self, val):
        self.stackIn.append(val)
    
    def dequeue(self):
        if not self.stackIn and not self.stackOut:
            return -1

        self.peek()
        return self.stackOut.pop()
    
    def peek(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        return self.stackOut[-1]
    
    def empty(self):
        return not self.stackIn and not self.stackOut

if __name__ == '__main__': 
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.peek())


