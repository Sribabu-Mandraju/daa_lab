import heapq

def dikstras(graph,start):
    priority_que = [(0,start)]
    distances = { node: float('infinity') for node in graph}
    distances[start] = 0
    while priority_que:
        current_distance,current_node = heapq.heappop(priority_que)
        if current_distance > distances[current_node]:
            continue
        
        for neighbour,weight in graph[current_node]:
            distance = current_distance+weight
            if distance < distances[neighbour]:
                distance[neighbour] = distance
                heapq.heappush(priority_que,(weight,neighbour))
    return distances


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_paths = dikstras(graph, start_node)

print("Shortest distances from node", start_node, ":", shortest_paths)
