# Floyd-Warshall Algorithm using Dynamic Programming
def floyd_warshall(graph):
    n = len(graph)
    
    # Initialize distance matrix the same as the graph's adjacency matrix
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    # Iterate through each node as an intermediate node
    for k in range(n):
        # Pick all pairs of nodes (i, j)
        for i in range(n):
            for j in range(n):
                # If i -> k -> j is shorter than i -> j, update dist[i][j]
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example graph as an adjacency matrix
# 0 represents the distance to itself, float('inf') represents no direct path between nodes
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

# Find shortest paths using Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Display the shortest path distance matrix
print("Shortest path matrix:")
for row in shortest_paths:
    print(row)
