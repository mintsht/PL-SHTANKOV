# Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный
# элементы и поменять их с первым и последним элементами строки соответственно.

filename_in = "10_1_2_Штаньков_Даниил_Александрович_УБ_vvod.txt"
filename_out = "10_1_2_Штаньков_Даниил_Александрович_УБ_vivod.txt"

# cчитывает матрицу из файла, меняет местами максимальный и минимальный элементы в каждой строке с крайними, и
# записывает измененную матрицу в файл.
def matrix(filename_in, filename_out):
    with open(filename_in, 'r') as f_in:
        # читаем размеры матрицы из первой строки файла (N M)
        N, M = map(int, f_in.readline().split())
        # map – это встроенная функция, которая применяет заданную функцию к каждому элементу последовательности
        # (например, списка) и возвращает итератор с результатами
        # split – это метод строк в Python, который разбивает строку на подстроки на основе заданного разделителя
        # и возвращает список этих подстрок.

        # читаем матрицу из файла построчно
        b = []

        for _ in range(N): # используем "_" в циклах, чтобы показать, что эта переменная не применяется в вычислениях
                           # и не имеет никакого значения

            matrix_str = f_in.readline().strip()
            matrix = [int(x) for x in matrix_str.split()]
            b.append(matrix)

    # обрабатываем каждую строку матрицы
    # перебираем строки матрицы
    for i in range(N):
        matrix = b[i]  # текущая строка

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

    # записываем измененную матрицу в выходной файл
    with open(filename_out, 'w') as f_out:
        f_out.write(f"{N} {M}\n")  # Записываем размеры матрицы
        for matrix in b:
            f_out.write(" ".join(map(str, matrix)) + "\n") # Записываем строки матрицы
            # join – это метод строк в Python, который объединяет элементы последовательности (например, списков
            # или кортежей) в одну строку, разделённую заданным строковым разделителем
            # map – это встроенная функция, которая применяет заданную функцию к каждому элементу последовательности
            # (например, списка) и возвращает итератор с результатами
            # str() используется для преобразования других типов данных в строку

matrix(filename_in, filename_out)