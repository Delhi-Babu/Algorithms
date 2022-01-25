class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class binaryTree:
    root = None
    def setData(self):
        self.root = Node(4,Node(5),Node(2,Node(3,Node(6),Node(7)),Node(1)))
        
        
    def frontView(self):
        currentNode = self.root
        data = []
        visited = []
        visited.append(currentNode)
        level = [0]
        currentLevel = 0
        data.append(currentNode.value) 
        while(visited):
            currentNode = visited.pop()
            if(currentNode.left):
                visited.append(currentNode.left)
                currentLevel+=1
                if(currentLevel not in level):
                    data.append(currentNode.value)
                    level.append(currentLevel)
                    
                print(level)
            if(currentNode.right):
                visited.append(currentNode.right)
        print(data)

tree = binaryTree()
tree.setData()
tree.frontView()
