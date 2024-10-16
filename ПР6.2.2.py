#2.2
a = [int(l) for l in input().split()]
b = []
m = []
for i in a:
    if -i == -abs(i):
        b.append(i)
    else:
        m.append(i)
print('Положительные элементы массива:', b)
print('Отрицательные элементы массива:', m)