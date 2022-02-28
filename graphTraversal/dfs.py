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

    def dft(self,node,arr,visited):
        if(node not in visited):
            arr.append(node)
            visited.add(node)
        if(self.adjacentList[node]):
            for i in self.adjacentList[node]:
                if(i not in visited):
                    self.dft(i,arr,visited)
        return arr
                    
    def dfs(self,start):
        return self.dft(start,[], set())

graph = DirectedGraph(False)
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

print(graph.adjacentList)
print(graph.dfs(1))
