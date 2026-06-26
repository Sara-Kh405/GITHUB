import numpy as np

#داده های اموزشی

patterns = np.array([[2, 2], [1, -2], [-2, 2], [-1, 1]])
targets = np.array([0, 1, 0, 1])

#مقداردهی به وزن ها و بایاس

W = np.array([0.0, 0.0])
b = 0.0

#نرخ یادگیری (در این قانون معمولا ۱ است)
lr = 1

#تابع فعالساز (یا ۰ یا ۱)

def hardlim(x):
    return 1 if x >= 0 else 0

#اموزش به صورت نمایشی ساده

print("learning Perseptron")
for epoch in range(5):  #چند تکرار کامل
    print(f"\nEpoch {epoch+1}")
    all_correct = True
    for i in range(len(patterns)):
        p = patterns[i]
        t = targets[i]
        
        #محاسبه خروجی
        a = hardlim(np.dot(W, p) + b)
        
        #محاسبه خطا
        e = t - a 
       
        if e != 0:
            
            all_correct = False
            W = W + e * p
            b = b + e 
            
            print(f"input{p}, target{t}, output{a}, error{e}, weight{W}, bias{b}")
       
    if all_correct:
        print("All samples are correct!!")
        break
       
     
#تست نهایی

print("Final test")
for i in range(len(patterns)):
    p = patterns[i]
    t = targets[i]
    a = hardlim(np.dot(W, p) + b)
    print(f"input {p}, target {t},output {a} -> {'correct' if a == t else 'incorrect'}")
    