from itertools import combinations #ساخت همه زیر مجموعه های ممکن

def tsp(graph):

    n = len(graph)

    g = {}
    J = {}

    # حالت پایه
    for i in range(1, n): # همه ی شهرها به جز شهر شروع
        g[(i, frozenset())] = graph[i][0] # S = {}

    # پر کردن جدول DP
    for size in range(1, n - 1):

        for i in range(1, n):

            others = [x for x in range(1, n) if x != i] # i همه شهرها به جز 

            for S in combinations(others, size): #تولید زیر مجموعه ها

                S = frozenset(S)

                best = float("inf")
                best_city = None

                for j in S:        #S = {j1, j2,  ...}

                    cost = graph[i][j] + g[(j, S - {j})] 

                    if cost < best:      #انتخاب min
                        best = cost
                        best_city = j

                g[(i, S)] = best
                J[(i, S)] = best_city    #بازیابی بهترین مسیرها

    # محاسبه جواب نهایی
    S = frozenset(range(1, n))

    answer = float("inf")
    first_city = None

    for j in S:

        cost = graph[0][j] + g[(j, S - {j})]

        if cost < answer:
            answer = cost
            first_city = j

    # بازیابی مسیر
    path = [0]

    current = first_city
    remaining = set(S)

    while current is not None:

        path.append(current)

        remaining.remove(current)

        current = J.get((current, frozenset(remaining)))

    path.append(0)

    return answer, path


n = int(input("Number of cities : "))

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

cost, path = tsp(graph)

print("Minimum Cost =", cost)

print("Path:")
for city in path:
    print(city + 1, end=" -> ")