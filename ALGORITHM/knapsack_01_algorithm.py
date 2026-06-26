#هرس کردن

def merge(S_prev, S1):
    combined = S_prev.union(S1)
    sorted_items = sorted(list(combined), key=lambda x: x[1]) # مرتب‌سازی بر اساس وزن
    
    result = []
    max_p = -1
    for p, w in sorted_items:
        if p > max_p:
            result.append((p, w))
            max_p = p
    return set(result)

def dpknapsack(p, w, n, M):
    S = [set() for _ in range(n + 1)]
    S[0] = {(0, 0)}
    
    for i in range(1, n + 1):
        S1 = set()
        pi, wi = p[i-1], w[i-1]
        for (P1, W1) in S[i-1]:
            if W1 + wi <= M:
                S1.add((P1 + pi, W1 + wi))
        
        S[i] = merge(S[i-1], S1)
    
    # پیدا کردن بهترین (P, W) در S[n]
    best_p, best_w = max(S[n], key=lambda x: x[0])
    
    # بازسازی مسیر (x[i])
    x = [0] * n
    curr_p, curr_w = best_p, best_w
    
    for i in range(n, 0, -1):
        if (curr_p, curr_w) not in S[i-1]:
            x[i-1] = 1
            curr_p -= p[i-1]
            curr_w -= w[i-1]
            
    return best_p, x

# ورودی‌ها طبق خواسته شما
# آیتم‌ها: (ارزش, وزن)
values = [1, 10, 4, 20]
weights = [3, 5, 7, 10]
n = 4
capacity = 20

best_val, selected_items = dpknapsack(values, weights, n, capacity)

print(f"The most worth is : {best_val}")
print(f"The selection item (1 means selected) : {selected_items}")

print("*******************************************")

objects = []
for i in range(len(selected_items)):
    if selected_items[i] == 1:
        objects.append(i+1)
print(f"The selection items are : objects{objects}")