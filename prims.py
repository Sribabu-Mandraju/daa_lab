import heapq

def prims_algorithm(graph, start):
    # Priority queue to store the edges
    min_heap = []
    
    # Set to track visited nodes
    visited = set()
    
    # List to store the edges of the MST
    mst_edges = []
    
    # Initialize total weight of MST
    total_weight = 0

    # Add the starting node to the heap with a weight of 0
    heapq.heappush(min_heap, (0, start))  # (weight, vertex)
    
    while min_heap:
        # Get the edge with the smallest weight
        weight, current_node = heapq.heappop(min_heap)

        # If the node has already been visited, skip it
        if current_node in visited:
            continue

        # Mark the node as visited
        visited.add(current_node)
        
        # If weight is not 0, add it to the MST edges (ignore the initial 0 weight for the start node)
        if weight > 0:
            mst_edges.append((weight, current_node))
            total_weight += weight
        
        # Explore all adjacent nodes and add them to the priority queue
        for neighbor, edge_weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
    
    return mst_edges, total_weight

# Example graph represented as an adjacency list (with weights)
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2, 'D': 4},
    'C': {'A': 3, 'B': 2, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

# Run Prim's algorithm starting from vertex 'A'
mst_edges, total_weight = prims_algorithm(graph, 'A')

# Display the edges in the MST and the total weight
print("Edges in the Minimum Spanning Tree:")
for weight, node in mst_edges:
    print(f"Weight: {weight}, Node: {node}")

print(f"\nTotal weight of MST: {total_weight}")
