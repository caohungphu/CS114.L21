from sys import stdin
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if(node==None):
            self.root = TreeNode(value)
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value)
            elif(value>node.data):
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value)
            else:
                return

    def getHeight(self, node):
        if node == None:
            return 0
        lNode = self.getHeight(node.left)
        rNode = self.getHeight(node.right)
        return max(lNode, rNode) + 1
            
f = deque()
tree = Tree()

while True:
    a = [int(x) for x in stdin.readline().split()]
    if a[0] == 0:
        f.appendleft(a[1])
    elif a[0] == 1:
        f.append(a[1])
    elif a[0] == 2:
        try:
            i = f.index(a[1])
            f.insert(i + 1,(a[2]))
        except:
            f.appendleft(a[2])
    else:
        for i in f:
            tree.addNode(tree.root, i)
        print(tree.getHeight(tree.root))
        exit()