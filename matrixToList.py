def matrix_to_adj_list(matrix):
    adj_list = {}
    
    # Iterate through each row in the matrix
    for i in range(len(matrix)):
        adj_list[i] = []
        
        # Iterate through each element in the row
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:  # If there's an edge, add it to the adjacency list
                adj_list[i].append(j)
    
    return adj_list

# Example adjacency matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# Convert the matrix to an adjacency list
adj_list = matrix_to_adj_list(matrix)

# Print the adjacency list
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")
