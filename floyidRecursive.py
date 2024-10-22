# Recursive Floyd-Warshall Algorithm
def floyd_warshall_recursive(graph, dist, k, i, j):
    # Base case: If we've considered all nodes as intermediates
    if k < 0:
        return dist[i][j]
    
    # Recursively calculate the shortest path considering node k
    return min(floyd_warshall_recursive(graph, dist, k - 1, i, j),
               dist[i][k] + dist[k][j])

def floyd_warshall(graph):
    n = len(graph)
    
    # Initialize distance matrix the same as the graph's adjacency matrix
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    # Use the recursive function to compute the shortest paths
    for i in range(n):
        for j in range(n):
            dist[i][j] = floyd_warshall_recursive(graph, dist, n - 1, i, j)
    
    return dist

# Example graph as an adjacency matrix
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

# Find shortest paths using the recursive Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Display the shortest path distance matrix
print("Shortest path matrix:")
for row in shortest_paths:
    print(row)
