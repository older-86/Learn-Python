# 4. Определить, какое число в массиве встречается чаще всего.

import random

print('Решение задачи №4')
n = 30
a, b = 0, 10

num, index_num, y = 0, 0, 0

array_1 = [random.randint(a, b) for _ in range (n)]
array_2 = []

print('Массив: ', array_1)

while a <= b:
    x = 0
    for i in array_1:
        if i == a:
            x = x + 1
    array_2.append(x)
    a += 1

print(array_2)

for i in array_2:
    if i > index_num:
        index_num = i
        num = y
    y += 1

print('Число {} больше всего встречается в массиве - {}'.format(num, index_num))
