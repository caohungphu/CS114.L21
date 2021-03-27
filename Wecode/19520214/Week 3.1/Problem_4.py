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

def countLeaf(node):
    if node == None:
        return 0
    else:
        if not node.left and not node.right:
            return 1
        else:
            return countLeaf(node.left) + countLeaf(node.right)
            

tree = Tree()


while True:
    n = int(input())
    if n == 0:
        print(countLeaf(tree.root))
        exit()
    else:
        tree.addNode(tree.root, n)


