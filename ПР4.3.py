# 3
a = int(input())
b = int(input())
while a > b:
    if a % 2 == 0:
        print(a - 1, end=" ")
        a = a - 2
    if a % 2 != 0:
        print(a, end=" ")
        a = a - 1