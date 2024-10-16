#1.2
import random as r

def g(s, mn, mx):
    return r.sample(range(mn, mx + 1), s)

def c(arr):
    t = sum(arr)
    m = t / len(arr) if arr else 0
    return t, m

n = 3
max_s = 15
mn = -100
mx = 100
a = []

for _ in range(n):
    s = r.randint(1, max_s)
    u = g(s, mn, mx)
    a.append(u)

for i, arr in enumerate(a):
    total, mean = c(arr)
    print(f"Массив {i + 1}: {arr}")
    print(f"Сумма: {total}, Среднее арифметическое: {mean:.2f}")