# Python implementation of Binary Search Tree 

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l:
            return self._find(val, node.l)
        elif val > node.v and node.r:
            return self._find(val, node.r)

    def delete_tree(self):
        # garbage collector will do this for us.
        if self.root:
            self.root = None

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.l)
            print(node.v, end = " ")
            self._view_tree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.view_tree()
print(tree.find(3).v)
print(tree.find(10))
tree.delete_tree()
tree.view_tree()