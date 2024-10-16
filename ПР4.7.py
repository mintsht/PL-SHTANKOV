#7
a = 1
b = 0
n = int(input())
for i in range(1, n + 1):
    b = b + a * i
    a *= i
print(b)