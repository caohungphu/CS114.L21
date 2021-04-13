import sys
input = sys.stdin.readline
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
def countLeafNode(self):
    if (self is None): return 0
    if (self.left is None and self.right is None):
        return 1
    return countLeafNode(self.left) + countLeafNode(self.right)

i = int(input())
res = []
root = Node(i)
while 1:
    i = int(input())
    if i==0:
        break
    root.insert(i)
print(countLeafNode(root))