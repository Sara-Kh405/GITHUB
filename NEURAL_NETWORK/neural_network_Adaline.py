import numpy as np

patterns = np.array([[1, 1], [1, -1], [-1, 1]])
targets = np.array([1, 1, -1])

w = np.array([0.0, 0.0])
b = 0.0

R = np.array([[1, -1/3, 1/3], [-1/3, 1, 1/3], [1/3, 1/3, 1]])

spesial_numbers = np.linalg.eigvals(R)
print(spesial_numbers)

lr = 0.1

print("learning Adaline")
for epoch in range(10):
    print(f"\nEpoch {epoch+1}")
    all_correct = True
    for i in range(len(patterns)):
        p = patterns[i]
        t = targets[i]

        #محاسبه خروجی
        a = np.dot(w, p) + b

        #محاسبه خطا
        e = t - a 
       
        if e != 0:
            
            print(f"BEFORE EDIT ***** input : {p}, target : {t}, output : {a}, error : {e}, weight : {w}, bias : {b}")
            all_correct = False
            w = w + (2 * lr * e * p.T)
            b = b + (2 * lr * e) 
            print(f"AFTER EDIT ***** input : {p}, target : {t}, output : {a}, error : {e}, weight : {w}, bias : {b}")

    if all_correct:
        print(f"bias is : {b}, weight is : {w}")
        break