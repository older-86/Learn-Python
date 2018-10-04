# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

print('Решение задачи №9')

a, b = 4, 4
array_min = []

matrix_1 = [[random.randint(1, 10) for _ in range (a)] for _ in range (b)]

for line in matrix_1:
    print(line)

print()

matrix_2 = list(zip(*matrix_1))

# for line in matrix_2:
#     print(line)

num_min = [0]*len(matrix_2[0])

for line in matrix_2:
    x = 11
    for i, item in enumerate (line):
        num_min [i] = item
        if x > num_min [i]:
            x = num_min [i]
    array_min.append(x)

print(array_min)

num_max, y = 0, 0
for i in array_min:
    if i > num_max:
        num_max = i
    y += 1

print('Максимум среди минимумов столбцов = {}'.format(num_max))