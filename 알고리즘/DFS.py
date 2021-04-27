from Graph import Graph

class DFS:
    def __init__(self,graph):
        self.v = 0
        self.g = graph
        self.visited = []
        for i in range(len(self.g)):
            self.visited.append(0)

    def dfs(self,v):
        self.v = v
        self.visited[v] = 1
        print("visited vertax : "+str(v))
        for i in range(len(self.g)):
            if self.g[v][i] != 0 and self.visited[i] == 0:
                self.visited[i] = 1
                self.dfs(i)


G = Graph(8)
G.insert_edge(0,1)
G.insert_edge(0,2)
G.insert_edge(1,3)
G.insert_edge(1,4)
G.insert_edge(2,5)
G.insert_edge(2,6)
G.insert_edge(3,7)
G.insert_edge(4,7)
G.insert_edge(5,7)
G.insert_edge(6,7)
graph = G.Graph_return()
p = DFS(graph)
p.dfs(0)
