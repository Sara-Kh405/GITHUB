# تعداد راس ها و یال ها
n = int(input("Please enter number of nodes: "))
m = int(input("Please enter number of edges: "))

# ماتریس مجاورت
graph = [[0] * n for _ in range(n)]

print("Enter origin, destination, weight : ")

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w

start = int(input("starting node: "))

# برچسب ها 
dist = [float('inf')] * n
dist[start] = 0

# راس های بازدید شده
visited = [False] * n

path = [[0] * n for _ in range(n)]  #*******
path[start][start] = 1

for _ in range(n):

    # پیدا کردن راس با کمترین فاصله
    min_dist = float('inf')
    u = -1

    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    visited[u] = True
    
    
    # به روزرسانی فاصله برچسب ها
    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

                #کپی مسیر u  
                path[v] = path[u][:]
                path[v][v] = 1

for i in range(n):
    print(path[i])

print('\nThe shortest distance:')

for i in range(n):
    print(f"{start} -> {i} = {dist[i]}")

