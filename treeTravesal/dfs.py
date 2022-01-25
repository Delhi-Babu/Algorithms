class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    root = None
    def insertNode(self,value):
        currentNode = self.root
        if(not currentNode):
            self.root = Node(value)
        else:
            while(currentNode):
                if(currentNode.value > value):
                    if(currentNode and not currentNode.left):
                        currentNode.left = Node(value)
                        return
                    currentNode = currentNode.left
                else:
                    if(currentNode and not currentNode.right):
                        currentNode.right = Node(value)
                        return
                    currentNode = currentNode.right

    def InOrderTraverse(self,node,data):
        if(node.left):
            self.InOrderTraverse(node.left,data)
        data.append(node.value)
        if(node.right):
            self.InOrderTraverse(node.right,data)
        return data

    def dfsInorder(self):
        return self.InOrderTraverse(self.root,[])

    def PreOrderTraverse(self,node,data):
        data.append(node.value)
        if(node.left):
            self.PreOrderTraverse(node.left,data)
        if(node.right):
            self.PreOrderTraverse(node.right,data)
        return data

    def dfsPreOrder(self):
        return self.PreOrderTraverse(self.root,[])

    def PostOrderTraverse(self,node,data):
        if(node.left):
            self.PostOrderTraverse(node.left,data)
        if(node.right):
            self.PostOrderTraverse(node.right,data)
        data.append(node.value)
        return data

    def dfsPostOrder(self):
        return self.PostOrderTraverse(self.root,[])





tree = BinarySearchTree()
arr = [99,52,1,33,30,80,59]


# arr = [15,6,4,5,7,23,71,50]
# arr = [88,62,14,54,41,31,27,76,64,63,75]
for i in arr:
    tree.insertNode(i)
print(tree.dfsInorder())
print(tree.dfsPreOrder())
print(tree.dfsPostOrder())
