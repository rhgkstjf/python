class Graph:
    def __init__(self,size):
        self.size = size
        self.g = []
        for i in range(self.size):
            row = []
            for k in range(self.size):
                row.append(0)
            self.g.append(row)
        
    def print_Graph(self):
        print(self.g)

    #가중치 없는 간선 삽입 그래프 만들때 사용
    def insert_edge(self,start,end):
        if start == end:
            return
        elif start >= self.size or end >= self.size:
            return
        elif self.g[start][end] != 0 and g[end][start] != 0:
            return
        else:
            self.g[start][end] = 1
            self.g[end][start] = 1

    #가중치 있는 간선 삽입 그래프 만들때 사용
    def insert_edge_weight(self,start,end,weight):
        if start == end:
            return
        elif start >= self.size or end >= self.size:
            return
        elif self.g[start][end] != 0 and g[end][start] != 0:
            return
        else:
            self.g[start][end] = weight
            self.g[end][start] = weight

    def Graph_return(self):
        return self.g
