

"""matrix = {
    "A" : [0, 1, 1, 0, 0, 0],
    "B" : [1, 0, 0, 1, 1, 0],
    "C" : [1, 0, 0, 0, 0, 1],
    "D" : [0, 1, 0, 0, 0, 0],
    "E" : [0, 1, 0, 0, 0, 0],
    "F" : [0, 0, 1, 0, 0, 0]
}
"""
matrix = {
    "A" : [0, 1, 1, 0, 0, 0, 0, 0],
    "B" : [0, 0, 0, 1, 1, 0, 0, 0],
    "C" : [1, 0, 0, 0, 0, 1, 1, 0],
    "D" : [0, 1, 0, 0, 0, 0, 0, 0],
    "E" : [0, 1, 0, 0, 0, 0, 0, 1],
    "F" : [0, 0, 1, 0, 0, 0, 0, 0],
    "G" : [0, 0, 1, 0, 0, 0, 0, 0],
    "H" : [0, 0, 0, 0, 1, 0, 0, 0]
}

nodes = list(matrix.keys())
visited = set()

def Re_DFS(matrix, start):
    visited.add(start)
    print(start, end="")
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and nodes[i] not in visited:
            Re_DFS(matrix, nodes[i])

Re_DFS(matrix, "A")


    
