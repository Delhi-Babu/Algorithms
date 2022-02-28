class DirectedGraph:
    def __init__(self, isDirected):
        self.isDirected = isDirected
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self,value):
        self.adjacentList[value] = []
        self.numberOfNodes+=1

    def addEdge(self,start,end):
        self.adjacentList[start].append(end)
        if(not self.isDirected):
            self.adjacentList[end].append(start)

    def printGraph(self):
        for i in self.adjacentList.items():
            print(f"{i[0]} -->",end="")
            for j in i[1]:
                print(j, end=" ")
            print()

    def bfs(self,start):
        data = []
        queue = []
        queue.append(start)
        if(self.isDirected):
            while queue:
                if(queue and queue[0] not in data):
                    data.append(queue[0])
                currentNode = self.adjacentList[queue.pop(0)]
                for i in currentNode:
                    queue.append(i)
        else:
            visited = set()
            queue.append(start)
            while queue:
                if(queue and queue[0] not in visited):
                    data.append(queue[0])
                    visited.add(queue[0])
                currentNode = self.adjacentList[queue.pop(0)]
                for i in currentNode:
                    if(i not in visited):
                        queue.append(i)

        return data





graph = DirectedGraph(False)
# graph.addVertex(1)
# graph.addVertex(2)
# graph.addVertex(3)
# graph.addVertex(4)
# graph.addVertex(5)
# graph.addVertex(6)

# graph.addEdge(1,2)
# graph.addEdge(1,3)
# graph.addEdge(2,4)
# graph.addEdge(4,3)
# graph.addEdge(3,5)
# graph.addEdge(5,6)


# # 1->2
# # |  |
# # 3<-4
# # |
# # 5->6

# graph.printGraph()
# print(graph.adjacentList)
# print(graph.bfs(1))

graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)

graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(3,5)
graph.addEdge(5,6)


print(graph.bfs(1))
print(graph.adjacentList)
