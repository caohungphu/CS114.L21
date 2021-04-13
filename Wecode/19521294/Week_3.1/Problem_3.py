import sys
import collections
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data is not None:
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

def height(root):    
        if(root is None):
            return 0
        else:
            return 1+max(height(root.left), height(root.right))
link_list = collections.deque()
while 1:
    knumber=list(map(int,input().split()))
    key = knumber[0]
    if key == 3:
        break
    elif key == 0:
        link_list.appendleft(knumber[1])
    elif key == 1:
        link_list.append(knumber[1])
    else:
        if knumber[1] not in link_list:
            link_list.insert(0,knumber[2])
        else:
            ind = link_list.index(knumber[1]) + 1
            link_list.insert(ind,knumber[2])
if link_list:
    root = Node(link_list[0])
    link_list.popleft()
    if link_list:
        for i in link_list:
            root.insert(i)
    print(height(root))
else:
    print(0)