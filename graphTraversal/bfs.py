class DirectedGraph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self,value):
        self.adjacentList[value] = []
        self.numberOfNodes+=1

    def addEdge(self,start,end):
        self.adjacentList[start].append(end)

    def printGraph(self):
        for i in self.adjacentList.items():
            print(f"{i[0]} -->",end="")
            for j in i[1]:
                print(j, end=" ")
            print()
    def bfs(self,start):
        data = []
        queue = []
        data.append(queue)
        queue.append(start)
        while queue:
            if(queue):
                data.append(queue[0])
            currentNode = self.adjacentList[queue.pop(0)]
            for i in currentNode:
                queue.append(i)
        return data





graph = DirectedGraph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')

graph.addEdge('a','c')
graph.addEdge('a','b')
graph.addEdge('b','d')
graph.addEdge('c','e')
graph.addEdge('d','f')


# 1->2
# |  |
# 3<-4
# |
# 5->6

graph.printGraph()
print(graph.adjacentList)
print(graph.bfs('a'))
