# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

print('Решение задачи №6')

a, x , y = 10, 0, 0

num_min, index_min = 101, 0
num_max, index_max = 0, 0

array_1 = [random.randint(0, 100) for _ in range (a)]

print('Первый массив: ', array_1)

for i in array_1:

    if i < num_min:
        num_min = i
        index_min = x
    x += 1

for i in array_1:
    if i > num_max:
        num_max = i
        index_max = y
    y += 1

print('Максимум = {}, минимум = {}'.format(num_max,num_min))
print('Индекс максимума = {}, индекс минимума = {}'.format(index_max,index_min))

if index_max > index_min:
    array_2 = array_1 [index_min + 1:index_max]
else:
    array_2 = array_1 [index_max +1 :index_min]

print('Второй массив: ', array_2)

print('Сумма элементов между минимумом и максимумом массива = {}'.format(sum(array_2)))
