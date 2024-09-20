'''
https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/
Implementation of Hash Table in Python using Separate Chaining
to avoid collisions

Main idea:
(key1, key2, ...) -> (hash function) -> Hash Table (index, value)
where index is the locaiton to insert a key, and value is the info mapped to a key.

Separate chaining is a technique used to handle collisions in a hash table. 
When two or more keys map to the same index in the array, we store them in a linked list at that index. 
This allows us to store multiple values at the same index and still be able to retrieve them using their key.
'''

class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            currentNode = self.table[index]
            while currentNode:
                if currentNode.key == key:
                    currentNode.value = value
                    return
            newNode = Node(key, value)
            newNode.next = self.table[index]
            self.table[index] = newNode
            self.size += 1
    
    def search(self, key):
        pass