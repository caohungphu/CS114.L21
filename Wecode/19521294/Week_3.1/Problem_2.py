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
    def PrintTree(self):    
        if(self is None):
            return
        else:
            queue = [self]
            res = []
            while queue:
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                res.append(queue[0].data)
                queue.pop(0)
        print(*res, " ")
i = int(input())
res = []
root = Node(i)
while 1:
    i = int(input())
    if i==0:
        break
    root.insert(i)
root.PrintTree()