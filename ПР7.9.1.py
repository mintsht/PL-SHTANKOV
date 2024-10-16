#9.1
a = int(input("Введите натуральное число a: "))
c = 0

def s(n):
    return sum(int(d) for d in str(n))

while a > 0:
    a -= s(a)
    if a > 0:
        print("Промежуточное значение:", a)
        c += 1
print("Промежуточное значение: 0")
print("Количество итераций:", c+1)
