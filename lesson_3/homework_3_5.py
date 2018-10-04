# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию
# в массиве.


import random

print('Решение задачи №5')
n = 10
a, b = -100, +100

num = a - 1
index_num, y = 0, 0


array_1 = [random.randint(a, b) for _ in range (n)]

print('Массив: ', array_1)

for i in array_1:
    if num < i < 0:
        num = i
        index_num = y
    y += 1

print('Максимум - {} с позицией - {}'.format(num, index_num))
