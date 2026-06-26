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

def DFS(matrix, start): 
    stack = [start]

    while len(stack) > 0:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            print(u, end="")
            for i in range(len(matrix)-1, -1, -1):
                if matrix[u][i] == 1:
                    stack.append(nodes[i])
  
DFS(matrix, "A")
