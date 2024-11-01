class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self,node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    
    def union(self,node1 , node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.root[root1] = root2
        else:
            self.root[root2] = root1
            self.rank[root1] +=1

def kruskal(edges,vertices):
    edges.sort(key = lambda x: x[2])
    uf = UnionFind(vertices)
    mst_edges = []
    total_weight = 0
    for u,v,weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            mst_edges.append((u,v,weight))
            total_weight += weight
    return mst_edges,total_weight

graph = {
    0: {1: 3, 2: 5, 3: 2, 4: 4, 5: 6, 6: 1, 7: 7, 8: 8, 9: 9},
    1: {0: 3, 2: 1, 3: 4, 4: 7, 5: 2, 6: 5, 7: 6, 8: 3, 9: 4},
    2: {0: 5, 1: 1, 3: 3, 4: 2, 5: 8, 6: 4, 7: 5, 8: 6, 9: 7},
    3: {0: 2, 1: 4, 2: 3, 4: 1, 5: 7, 6: 2, 7: 8, 8: 4, 9: 5},
    4: {0: 4, 1: 7, 2: 2, 3: 1, 5: 3, 6: 6, 7: 7, 8: 5, 9: 2},
    5: {0: 6, 1: 2, 2: 8, 3: 7, 4: 3, 6: 1, 7: 4, 8: 6, 9: 3},
    6: {0: 1, 1: 5, 2: 4, 3: 2, 4: 6, 5: 1, 7: 3, 8: 5, 9: 7},
    7: {0: 7, 1: 6, 2: 5, 3: 8, 4: 7, 5: 4, 6: 3, 8: 2, 9: 1},
    8: {0: 8, 1: 3, 2: 6, 3: 4, 4: 5, 5: 6, 6: 5, 7: 2, 9: 4},
    9: {0: 9, 1: 4, 2: 7, 3: 5, 4: 2, 5: 3, 6: 7, 7: 1, 8: 4}
}
edges = []

for u in graph:
    for v , weight in graph[u].items():
        if (u < v):
            edges.append((u,v,weight))
            
mst_edges, total_weight = kruskal(edges,10)
            
print("MST edges:", mst_edges)
print("MST weight:", total_weight)


