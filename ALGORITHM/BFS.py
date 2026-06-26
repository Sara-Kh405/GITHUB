
"""matrix = {
    "A" : [0, 1, 1, 0, 0, 0],
    "B" : [1, 0, 0, 1, 1, 0],
    "C" : [1, 0, 0, 0, 0, 1],
    "D" : [0, 1, 0, 0, 0, 0],
    "E" : [0, 1, 0, 0, 0, 0],
    "F" : [0, 0, 1, 0, 0, 0]
}"""

matrix  = {
    "A" : [0, 1, 1, 0, 0, 0, 0, 0],
    "B" : [1, 0, 0, 0, 0, 0, 0, 0],
    "C" : [1, 0, 0, 1, 0, 0, 0, 0],
    "D" : [0, 0, 1, 0, 1, 1, 0, 0],
    "E" : [0, 0, 0, 1, 0, 1, 1, 0],
    "F" : [0, 0, 0, 1, 1, 0, 1, 1],
    "G" : [0, 0, 0, 0, 1, 1, 0, 1],
    "H" : [0, 0, 0, 0, 0, 1, 1, 0]
}

nodes = list(matrix.keys())
visited = set()

def BFS(matrix, start): 
    queue = [start]

    while len(queue) > 0:
        u = queue.pop(0)
        if u not in visited:
            visited.add(u)
            print(u, end="")
            for i in range(len(matrix)):
                if matrix[u][i] == 1 and nodes[i] not in queue:
                    queue.append(nodes[i])
  
BFS(matrix, "E")