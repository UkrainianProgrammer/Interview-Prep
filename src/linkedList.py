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
        pass

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
            raise Exception("Index not found")
            



    def removeNode(self, val):
        pass

    def printAll(self):
        pass

    def sizeOfAll(self):
        pass

if __name__ == '__main__':
    pass