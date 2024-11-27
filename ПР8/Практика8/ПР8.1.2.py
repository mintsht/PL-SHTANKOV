# Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный
# элементы и поменять их с первым и последним элементами строки соответственно.

import random

# размеры матрицы
N = int(input("N=")) # количество строк
M = int(input("M=")) # количество столбцов

# создаем матрицу NxM со случайными целыми числами от -10 до 10
b = [[random.randint(-10, 10) for _ in range(M)] for _ in range(N)]

# выводим исходную матрицу
print("Матрица:")
for matrix in b:
    print(matrix)

# перебираем строки матрицы
for i in range(N):
    matrix = b[i] # текущая строка

    # находим максимальный и минимальный элементы в строке
    max_element = max(matrix)
    min_element = min(matrix)

    # находим индексы максимального и минимального элементов
    max_index = matrix.index(max_element)
    min_index = matrix.index(min_element)

    # меняем местами максимальный элемент и первый элемент строки
    matrix[max_index], matrix[0] = matrix[0], matrix[max_index]

    # меняем местами минимальный элемент и последний элемент строки
    matrix[min_index], matrix[-1] = matrix[-1], matrix[min_index]

# выводим измененную матрицу
print("Измененная матрица:")
for matrix in b:
    print(matrix)