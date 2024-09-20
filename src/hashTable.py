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
        index = self._hash(key)

        currentNode = self.table[index]
        while currentNode:
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)

        previousNode = None
        currentNode = self.table[index]
        while currentNode:
            if currentNode.key == key:
                if previousNode:
                    previousNode.next = currentNode.next
                else:
                    self.table[index] = currentNode.next
                self.size -= 1
                return
            previousNode = currentNode
            currentNode = currentNode.next
        raise KeyError(key)
    
    def __len__(self):
        return self.size
    
    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

if __name__ == '__main__': 
    # Create a hash table
    ht = HashTable(5)

    # add some key-value pairs
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)

    # check if hash table contains a key
    print("apple" in ht)
    print("peach" in ht)

    # Get the value for a key
    print(ht.search("banana"))

    # update the value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))

    # remove the key
    ht.remove("apple")
    
    # check the size
    print(len(ht))