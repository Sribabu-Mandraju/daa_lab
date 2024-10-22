from collections import deque

def bfs(graph, start_node):
    # Initialize a queue for BFS and a set to keep track of visited nodes
    queue = deque([start_node])
    visited = set([start_node])
    
    # Loop until there are no more nodes to explore
    while queue:
        # Pop the first node from the queue
        current_node = queue.popleft()
        print(current_node, end=" ")  # Process the current node (e.g., print it)
        
        # Explore all the neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Add the neighbor to the queue

# Example graph (as an adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call BFS starting from node 'A'
bfs(graph, 'A')
