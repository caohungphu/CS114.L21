class Node:

      def __init__(self,info): #constructor of class

          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined

      def __str__(self):

          return str(self.info) #return as string
class searchtree:
      def __init__(self): 

          self.root = None
      def getRoot(self):
            return self.root
      def create(self,val):  

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
def _demla(root):
    if root == None:
        return 0
    else:
        if root.left == None and root.right == None:
            return 1
        else:
            return _demla(root.left) + _demla(root.right)
        
tree = searchtree()
while True:
    n = int(input())
    if n == 0:
        break
    else:
        tree.create(n)
print(_demla(tree.getRoot()))