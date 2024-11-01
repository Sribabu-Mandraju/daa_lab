class UnionFind:
    def __init__(self, size):
        # Initialize the Union-Find structure with `size` nodes.
        # Each node is its own root initially.
        self.root = [i for i in range(size)]
        # Rank array to keep track of the tree depth for union by rank
        self.rank = [0] * size

    def find(self, node):
        # Find the root of the node with path compression.
        # This will flatten the structure of the tree whenever find is called.
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])  # Path compression
        return self.root[node]

    def union(self, node1, node2):
        # Union two nodes by connecting their roots.
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by rank: attach the shorter tree under the root of the taller tree
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1  # Increase rank if both trees were the same height

def kruskals_algorithm(edges, num_nodes):
    # Sort edges based on their weights (ascending order)
    edges.sort(key=lambda x: x[2])  # Sort by weight

    # Create a Union-Find object for managing connected components
    uf = UnionFind(num_nodes)
    mst_edges = []  # List to hold edges in the Minimum Spanning Tree (MST)
    total_weight = 0  # Total weight of the MST

    for u, v, weight in edges:
        # Check if adding this edge would form a cycle
        if uf.find(u) != uf.find(v):
            # If they belong to different sets, union them
            uf.union(u, v)
            mst_edges.append((u, v, weight))  # Add edge to the MST
            total_weight += weight  # Add weight to the total

    return mst_edges, total_weight  # Return the edges of the MST and the total weight

# Graph represented as an adjacency list
graph = {
    0: [(1, 1), (2, 3)],  # Node 0 connects to Node 1 with weight 1 and Node 2 with weight 3
    1: [(0, 1), (2, 2), (3, 4)],  # Node 1 connects to Nodes 0, 2, and 3
    2: [(0, 3), (1, 2), (3, 5)],  # Node 2 connects to Nodes 0, 1, and 3
    3: [(1, 4), (2, 5)]  # Node 3 connects to Nodes 1 and 2
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

# Run Kruskal's algorithm to find the MST
mst_edges, total_weight = kruskals_algorithm(edges, num_nodes)

# Display the edges in the MST and the total weight
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst_edges:
    print(f"Edge: ({u}, {v}), Weight: {weight}")

print(f"\nTotal weight of MST: {total_weight}")
