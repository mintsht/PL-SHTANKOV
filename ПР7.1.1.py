#1.1
import math
def i(f, data):
    if f == 'круг':
        res = math.pi * (data[0] ** 2)
    if f == 'прямоугольник':
        a, b = data
        res = a * b
    if f == 'треугольник':
        res = (a * b) / 2
    return 'Площадь {} = {}'.format(f, res)
figure = input('Фигура: ')
f = figure.lower()
data = [float(i) for i in input('данные через пробел: ').split()]
print(i(f, data))