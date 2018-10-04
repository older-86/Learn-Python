# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
# между собой (оба являться минимальными), так и различаться.

import random

print('Решение задачи №7')

a = 10

x, y = 0, 0

num_min_1, index_min_1 = 101, 0
num_min_2, index_min_2 = 101, 0

array_1 = [random.randint(0, 100) for _ in range (a)]


print('Первый массив: ', array_1)

for i in array_1:

    if i < num_min_1:
        num_min_1 = i
        index_min_1 = x
    x += 1

array_2 = array_1

array_2.remove(num_min_1)

for i in array_2:
    if i < num_min_2:
        num_min_2 = i
        index_min_2 = y
    y += 1

print('1 минимум = {}, 2 минимум = {}'.format(num_min_1,num_min_2))

# print('Индекс 1 минимума = {}, индекс 2 минимума = {}'.format(index_min_1,index_min_2))
print('Второй массив: ', array_1)
# print('Второй массив: ', array_2)