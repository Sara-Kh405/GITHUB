def knapsack(M):
    inputs = input("Please input the objects : ").split()
    weights = list(map(int, input("Please input the weights of objects : ").split()))
    worths = list(map(int, input("Please input the worths of objects : ").split()))

    objects = []

    for i in range(len(inputs)):
        objects.append({
            "name" : inputs[i],
            "weight" : weights[i],
            "worth" : worths[i],
            "ratio" : worths[i] / weights[i]
        })
    objects.sort(key=lambda x: x["ratio"], reverse=True)
    result = []
    total_worth = 0

    for obj in objects:
        if obj["weight"] <= M:
            result.append((obj["name"], 1))
            M -= obj["weight"]
            total_worth += obj["worth"]
        else:
            fraction = M / obj["weight"]
            result.append((obj["name"], fraction))
            total_worth += obj["worth"] * fraction
            M = 0
            break
    return result, total_worth

chosen, worth = knapsack(15)
print("Objects : ")
for name, frac in chosen:
    print(name, "->", frac)
print("Worth = ", worth)


    
    


