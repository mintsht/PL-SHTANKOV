#1.2
a = [int(l) for l in input().split()]
b = sum(a) / len(a)
a = [it if it else b for it in a]
print('Измененный масив:', a)