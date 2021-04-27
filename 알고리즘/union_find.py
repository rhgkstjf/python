class union_find:
    def __init__(self,size):
        self.size = size
        self.tree = []
        self.rank = []
        for i in range(self.size):
            self.rank.append(1)
    
    def set(self):
        for i in range(self.size):
            self.tree.append(-1)

    def find(self,x):
        sub = x
        while self.tree[x] != -1:
            x = self.tree[x]
        
        while self.tree[sub] != -1:
            parents = self.tree[sub]
            self.tree[sub] = x
            sub = self.tree[parents]

        return x
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        #루트가 같으면 안합침
        if x == y:
            return

        #가장 많은 자식을 가진 트리가 작은 트리를 먹는 형태
        if self.rank[x] < self.rank[y]:
            self.tree[x] = y
            self.rank[y] += self.rank[x]
        else:
            self.tree[y] = x
            self.rank[x] += self.rank[y]


#p = union_find(5)
#p.set()
#p.union(0,1)
#p.union(2,3)
#p.union(0,2)
#print(p.tree)
#print(p.rank)
