#Linked List

from sys import stdin

class Node: 
    def __init__(self, new_data): 
        self.data = new_data
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None
        self.tail = None
  
    def addHead(self, newNode):
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head 
            self.head = newNode
        
    def addTail(self, newNode): 
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def findX(self, x):
        tmp = self.head
        while tmp:
            if tmp.data == x:
                return tmp
            tmp = tmp.next
        return None

    def addAfter(self, preNode, newNode):
        newNode.next = preNode.next
        preNode.next = newNode
        return

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next

class TreeNode:
    def __init__(self, new_data):
        self.left = None
        self.right = None
        self.data = new_data

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, newNode):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = newNode
        else:
            if newNode.data < node.data:
                if node.left is None:
                    node.left = newNode
                    return 
                else:
                    return self.addNode(node.left, newNode)
            elif newNode.data > node.data:
                if node.right is None:
                    node.right = newNode
                    return 
                else:
                    return self.addNode(node.right, newNode)

    def printTree(self, node):
        if node == None:
            return 0
        print(node.data, end=" ")
        self.printTree(node.left)
        self.printTree(node.right)

    def getHeight(self, node):
        if node == None:
            return 0
        lNode = self.getHeight(node.left)
        rNode = self.getHeight(node.right)
        return max(lNode, rNode) + 1
            
tree = Tree()
linkedList = LinkedList()

while True:
    a = [int(x) for x in stdin.readline().split()]
    if a[0] == 0:
        newNode = Node(a[1])
        linkedList.addHead(newNode)

    elif a[0] == 1:
        newNode = Node(a[1])
        linkedList.addTail(newNode)

    elif a[0] == 2:
        if linkedList.head is None:
            linkedList.head = linkedList.tail = Node(a[2])
        else:
            preNode = linkedList.findX(a[1])
            newNode = Node(a[2])
            if preNode == None:
                linkedList.addHead(newNode)
            elif preNode == linkedList.tail:
                linkedList.addTail(newNode)
            else:
                linkedList.addAfter(preNode, newNode)

    else:
        temp = linkedList.head
        while (temp): 
            newNodeTree = TreeNode(temp.data)
            tree.addNode(tree.root, newNodeTree)
            temp = temp.next
        print(tree.getHeight(tree.root))
        exit()