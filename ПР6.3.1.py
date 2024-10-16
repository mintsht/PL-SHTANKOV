#3.1
a = [int(l) for l in input().split()]
s = []
for i in a:
    if a.index(i) % 2 != 0:
        s.append(i)
print(sum(int(i) for i in s))