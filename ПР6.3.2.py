#3.2
#1 способ
a = 8
b = []
for i in range(a):
    v = int(input('Введите элемент массива: '))
    if v < 15:
        v = v * 2
    b.append(v)
print('Измененный массив:', b)

#2 способ
a = [int(l) for l in input().split()]
b = []
for i in a:
    if i <= 15:
        i = i * 2
        b.append(i)
    else:
        b.append(i)
print('Измененный массив:', b)