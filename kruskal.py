class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])  # Path compression
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1

def kruskals_algorithm(edges, num_nodes):
    # Sort edges based on their weights
    edges.sort(key=lambda x: x[2])  # Sort by weight

    uf = UnionFind(num_nodes)
    mst_edges = []
    total_weight = 0

    for u, v, weight in edges:
        # Check if the current edge forms a cycle
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight

# Graph represented as an adjacency list
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 2), (3, 4)],
    2: [(0, 3), (1, 2), (3, 5)],
    3: [(1, 4), (2, 5)]
}

# Convert adjacency list to edge list format for Kruskal's algorithm
edges = []
for u in graph:
    for v, weight in graph[u]:
        # To avoid duplicates, only add edges where u < v
        if u < v:
            edges.append((u, v, weight))

# Number of nodes in the graph
num_nodes = len(graph)

# Run Kruskal's algorithm
mst_edges, total_weight = kruskals_algorithm(edges, num_nodes)

# Display the edges in the MST and the total weight
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst_edges:
    print(f"Edge: ({u}, {v}), Weight: {weight}")

print(f"\nTotal weight of MST: {total_weight}")
