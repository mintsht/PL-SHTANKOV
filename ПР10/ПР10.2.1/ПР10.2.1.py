# Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом,
# т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.

filename_in = "10_2_1_Штаньков_Даниил_Александрович_УБ_vvod.txt"
filename_out = "10_2_1_Штаньков_Даниил_Александрович_УБ_vivod.txt"

# проверяет, является ли квадратная матрица из файла магическим квадратом, и записывает результат в файл
def magic1(filename_in, filename_out):
    with open(filename_in, 'r') as f_in:
        # читаем размер матрицы из первой строки файла
        N = int(f_in.readline())

        # читаем матрицу из файла построчно
        b = []
        for _ in range(N):
            row_str = f_in.readline().strip()
            row = [int(x) for x in row_str.split()]
            b.append(row)

    # вычисляем сумму элементов первой строки
    sum_first_row = sum(b[0])

    # проверяем строки
    magic = True
    for i in range(1, N):
        if sum(b[i]) != sum_first_row:
            magic = False
            break

    # если все строки прошли проверку, проверяем столбцы
    if magic:
        for j in range(N):
            column_sum = sum(b[i][j] for i in range(N))
            if column_sum != sum_first_row:
                magic = False
                break

    # записываем результат в выходной файл
    with open(filename_out, 'w') as f_out:
        if magic:
            f_out.write("Матрица является магическим квадратом")
        else:
            f_out.write("Матрица не является магическим квадратом")

magic1(filename_in, filename_out)