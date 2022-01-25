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

    def bfs(self):
        currentNode = self.root
        data = []
        visited = []
        visited.append(currentNode)
        if(not currentNode):
            raise Exception("Empty tree found")
        else:
            while(visited):
                currentNode = visited.pop(0)
                if(currentNode.left):
                    visited.append(currentNode.left)
                if(currentNode.right):
                    visited.append(currentNode.right)
                data.append(currentNode.value)
        return data

    def breathFirstTraverseRecursion(self,visited,data):
        if(not visited):
            return data
        else:
            currentNode = visited.pop(0)
            data.append(currentNode.value)
            if(currentNode.left):
                visited.append(currentNode.left)
            if(currentNode.right):
                visited.append(currentNode.right)
            return self.breathFirstTraverseRecursion(visited,data)


    def bfsr(self):
        visited = []
        visited.append(self.root)
        # print(self.breathFirstTraverseRecursion(visited,[]))
        return self.breathFirstTraverseRecursion(visited, [])





tree = BinarySearchTree()
arr = [41,20,29,32,11,65,50,91,72,99,10]
# arr = [15,6,4,5,7,23,71,50]
# arr = [88,62,14,54,41,31,27,76,64,63,75]
for i in arr:
    tree.insertNode(i)
if(tree.bfs() == tree.bfsr()):
    print("success")
else:
    print("failure")
tree.bfsr()
tree.bfs()
