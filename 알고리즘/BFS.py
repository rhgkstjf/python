from Graph import Graph
from Queue import Queue

class BFS:
    def __init__(self,graph):
        self.size = len(graph)
        self.g = graph
        self.q = Queue(self.size)
        self.visited = []
        for i in range(self.size):
            self.visited.append(0)

    def bfs(self,v):
        self.q.Enqueue(v)
        self.visited[v] = 1
        print("visited vertax : "+ str(v))
        while self.q.is_empty() != True:
            v = self.q.Dequeue()
            for i in range(self.size):
                if self.g[v][i] == 1 and self.visited[i] == 0:
                    print("visited vertax : "+ str(i))
                    self.q.Enqueue(i)
                    self.visited[i] = 1




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

p = BFS(graph)
p.bfs(0)
