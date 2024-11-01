import heapq

def prims(graph, start):
    priority_que = []
    visited = set()
    mst_edges = []
    total_weight = 0
    heapq.heappush(priority_que, (0, start, None))  # Push initial node with weight 0

    while priority_que:
        weight, current, from_node = heapq.heappop(priority_que)

        if current in visited:
            continue
        visited.add(current)

        if from_node is not None:
            mst_edges.append((from_node, current))
            total_weight += weight

        for neighbour, edge_weight in graph[current].items():
            if neighbour not in visited:
                heapq.heappush(priority_que, (edge_weight, neighbour, current))

    return mst_edges, total_weight

graph = {
    "0": {"1": 3, "2": 5, "3": 2, "4": 4, "5": 6, "6": 1, "7": 7, "8": 8, "9": 9},
    "1": {"0": 3, "2": 1, "3": 4, "4": 7, "5": 2, "6": 5, "7": 6, "8": 3, "9": 4},
    "2": {"0": 5, "1": 1, "3": 3, "4": 2, "5": 8, "6": 4, "7": 5, "8": 6, "9": 7},
    "3": {"0": 2, "1": 4, "2": 3, "4": 1, "5": 7, "6": 2, "7": 8, "8": 4, "9": 5},
    "4": {"0": 4, "1": 7, "2": 2, "3": 1, "5": 3, "6": 6, "7": 7, "8": 5, "9": 2},
    "5": {"0": 6, "1": 2, "2": 8, "3": 7, "4": 3, "6": 1, "7": 4, "8": 6, "9": 3},
    "6": {"0": 1, "1": 5, "2": 4, "3": 2, "4": 6, "5": 1, "7": 3, "8": 5, "9": 7},
    "7": {"0": 7, "1": 6, "2": 5, "3": 8, "4": 7, "5": 4, "6": 3, "8": 2, "9": 1},
    "8": {"0": 8, "1": 3, "2": 6, "3": 4, "4": 5, "5": 6, "6": 5, "7": 2, "9": 4},
    "9": {"0": 9, "1": 4, "2": 7, "3": 5, "4": 2, "5": 3, "6": 7, "7": 1, "8": 4}
}

mst_edges, weight = prims(graph, "0")
print("MST edges:", mst_edges)
print("MST weight:", weight)
