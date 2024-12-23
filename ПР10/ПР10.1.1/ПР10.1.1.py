# Вычислить сумму и число положительных элементов матрицы A[N, N], находящихся над главной диагональю.

filename_in = "10_1_1_Штаньков_Даниил_Александрович_УБ_vvod.txt"
filename_out = "10_1_1_Штаньков_Даниил_Александрович_УБ_vivod.txt"

# считываем матрицу из файла, вычисляем сумму и количество положительных элементов над главной диагональю, и записываем
# результаты в другой файл.
def matrix(filename_in, filename_out):
    with open(filename_in, 'r') as f_in:
        # Читаем размер матрицы из первой строки файла
        N = int(f_in.readline())

        # Читаем матрицу из файла построчно
        a = []
        for _ in range(N):# используем "_" в циклах, чтобы показать, что
# эта переменная не применяется в вычислениях и не имеет никакого значения
            matrix_str = f_in.readline().strip()  # Читаем строку и убираем пробельные символы
            matrix = [int(x) for x in matrix_str.split()] # Преобразуем строку в список целых чисел
            # split – это метод строк в Python, который разбивает строку на подстроки на основе заданного разделителя
            # и возвращает список этих подстрок.

            a.append(matrix)

    sum_diagonal = 0  # инициализируем сумму элементов над главной диагональю
    positive_diagonal = 0  # инициализируем счетчик положительных элементов над главной диагональю

    # проходим по элементам матрицы, начиная с первого элемента над главной диагональю
    for i in range(N):
        for j in range(i + 1, N):  # j начинается со следующего элемента после диагонали (i+1)
            element = a[i][j]  # текущий элемент матрицы

            # добавляем элемент к сумме, если он положителен
            sum_diagonal += element

            # увеличиваем счетчик, если элемент положительный
            if element > 0:
                positive_diagonal += 1

    # Записываем результаты в выходной файл
    with open(filename_out, 'w') as f_out:
        f_out.write(f"Сумма элементов над главной диагональю: {sum_diagonal}\n")
        f_out.write(f"Количество положительных элементов над главной диагональю: {positive_diagonal}\n")

matrix(filename_in, filename_out)