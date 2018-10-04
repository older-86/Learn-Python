# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

print('Решение задачи №3')

a, x , y = 6, 0, 0

num_min, index_min = 101, 0
num_max, index_max = 0, 0

array_1 = [random.randint(0, 100) for _ in range (a)]
array_2 = array_1

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

array_2 [index_max] = num_min
array_2 [index_min] = num_max

print('Второй массив: ', array_2)



