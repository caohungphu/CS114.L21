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

    def BFS(self, node):
        to_visit = []
        if node:
            to_visit.append(node)
        while to_visit:
            current = to_visit.pop(0)
            print(current.data, end=" ")
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)
            

tree = Tree()


while True:
    n = int(input())
    if n == 0:
        tree.BFS(tree.root)
        exit()
    else:
        tree.addNode(tree.root, n)


