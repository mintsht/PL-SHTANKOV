#8.1
n = int(input("Введите натуральное число n: "))

def f(x):
    for i in range(1, x + 1):
        s = str(i)
        if all(int(d) != 0 and i % int(d) == 0 for d in s):
            print(i)
f(n)