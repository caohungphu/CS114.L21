from collections import deque
from sys import stdin
input = stdin.readline
class Node:

      def __init__(self,info): #constructor of class

          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined

      def __str__(self):

          return str(self.info) #return as string
def maxDepth(node):
    if node is None:
        return 0 ;  
    else :
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        return max(lDepth, rDepth) + 1
    return 0
 
class searchtree:

      def __init__(self): #constructor of class

          self.root = None
      def getRoot(self):
          return self.root 
      
      def create(self,val):  #create binary search tree nodes

          if self.root == None:

             self.root = Node(val)

          else:

             current = self.root

             while 1:

                 if val < current.info:

                   if current.left:
                      current = current.left
                   else:
                      current.left = Node(val)
                      break;      

                 elif val > current.info:
                 
                    if current.right:
                       current = current.right
                    else:
                       current.right = Node(val)
                       break;      

                 else:
                    break 
arr =[]   
f = deque()
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        #arr.insert(0,s[1])
        f.appendleft(s[1])
    elif s[0] == 1:
        f.append(s[1])
    elif s[0] == 2:
        try:
            x = f.index(s[1])
            f.insert(x+1,s[2])
        except:
            f.appendleft(s[2])
    else:
        break

tree = searchtree()     
for i in f:
    tree.create(i)
    
print(maxDepth(tree.getRoot()))