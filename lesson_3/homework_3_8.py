# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее
# последнюю ячейку. В конце следует вывести полученную матрицу.

import random

print('Решение задачи №8')

a, b = 4, 4
matrix_1 = []

for i in range (b):
    matrix_1.append([])
    for j in range(a):
        num = int(input('Введите данные для матрицы с клавиатуры: '))
        matrix_1[i].append(num)


#matrix_1 = [[random.randint(1, 10) for _ in range (a)] for _ in range (b)]

for line in matrix_1:
    print(line)

print()

for line in matrix_1:
    sum_line = 0

    for i, item in enumerate (line):
        sum_line += item
        print(f'{item:>3}', end='')

    print(f' | {sum_line}')

