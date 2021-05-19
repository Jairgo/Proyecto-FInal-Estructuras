from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s):
        print(s,"<- primer S\n")
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            #print(s,"<- S del ciclo")
            print(s, end = " ")

            for i in self.graph[s]:
                
                if visited[i] == False:
                    #print(i, end = " ")
                    queue.append(i)
                    visited[i] = True
            #print ("\n")

g = Graph()
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,0)
g.addEdge(3,2)
"""
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,5)
g.addEdge(1,6)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,0)
g.addEdge(3,1)
g.addEdge(3,2)
g.addEdge(3,4)
g.addEdge(4,2)
g.addEdge(4,3)
g.addEdge(4,6)
g.addEdge(5,1)
g.addEdge(5,2)
g.addEdge(6,1)
g.addEdge(6,4)
"""

print ("Aqui resultado")
g.BFS(0)