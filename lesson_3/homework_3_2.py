# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 0, 3, 4, 5 (индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят четные числа.

import random

print('Решение задачи №2')

a, x = 6, 0

array_1 = [random.randint(0,100) for _ in range (a)]
array_2 = []

print('Первый массив: ', array_1)

for i in array_1:
    if i % 2 == 0:
        array_2.append(x)
    x += 1

print('Второй массив: ', array_2)



