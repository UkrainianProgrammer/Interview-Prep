# Python implementation of Binary Search Tree

class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.val = None

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def addNode(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    
    def _add(self, val, node):
        if val < node.val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self.add(val, node.right)
            else:
                node.right = Node(val)
    
    def find(self, val):
        if self.root:
            return self._find(val, self.root)
        else:
            raise Exception(f'{val} does not exist in an empty Tree')
    
    def _find(self, val):
        pass