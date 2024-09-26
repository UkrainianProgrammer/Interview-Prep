class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtBegin(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def insertAtIndex(self, val, idx):
        if idx == 0:
            self.insertAtBegin(val)
            return

        pos = 0
        curNode = self.head
        while curNode != None and pos+1 != idx:
            pos += 1
            curNode = curNode.next
        if curNode != None:
            newNode = Node(val)
            newNode.next = curNode.next
            curNode.next = newNode
        else:
            raise Exception(f"Index {idx} not found")

    def updateNode(self, val, idx):
        curNode = self.head
        pos = 0
        if pos == idx:
            curNode.val = val
        else:
            while curNode != None and pos != idx:
                curNode = curNode.next
                pos += 1
            if curNode != None:
                curNode.val = val
            else:
                raise Exception(f"{val} at {idx} not found")

    def removeFirstNode(self):
        if self.head is None:
            return
        self.head = self.head.next

    def removeLastNode(self):
        if self.head is None:
            return
        curNode = self.head
        while curNode != None and curNode.next.next != None:
            curNode = curNode.next

        curNode.next = None
        

    def printAll(self):
        pass

    def sizeOfLL(self):
        size = 0
        if self.head:
            curNode = self.head
            while curNode != None:
                size += 1
                curNode = curNode.next
            return size
        else:
            return 0

if __name__ == '__main__':
    pass