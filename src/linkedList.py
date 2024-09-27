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

        while curNode != None and curNode.next.next != None:
            curNode = curNode.next

        curNode.next = None
    
    def removeNode(self, val):
        if self.head is None:
            return
        
        curNode = self.head
        while curNode != None and curNode.next.val != val:
            curNode = curNode.next
        
        if curNode == None:
            return
        else:
            curNode.next = curNode.next.next

    def printAll(self):
        if self.head:
            curNode = self.head
            while curNode:
                print(curNode.val)
                curNode = curNode.next
        else:
            raise Exception("Empty list")

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
    # create a new linked list
    llist = LinkedList()

    # add nodes to the linked list
    llist.insertAtEnd('a')
    llist.insertAtEnd('b')
    llist.insertAtBegin('c')
    llist.insertAtEnd('d')
    # llist.insertAtIndex('g', 2)

    # print the linked list
    print("Node Data")
    llist.printLL()

    # remove a nodes from the linked list
    print("\nRemove First Node")
    llist.remove_first_node()
    print("Remove Last Node")
    llist.remove_last_node()
    print("Remove Node at Index 1")
    llist.remove_at_index(1)

    # print the linked list again
    print("\nLinked list after removing a node:")
    llist.printLL()

    print("\nUpdate node Value")
    llist.updateNode('z', 0)
    llist.printLL()

    print("\nSize of linked list :", end=" ")
    print(llist.sizeOfLL())