# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

print('Решение задачи №3')

import random

m = 5
volume = 2 * m + 1
array_3 = [random.randint(0, 100) for _ in range(volume)]
print('Массив: {}'.format(array_3))


def medium(array):
    array_copy = array
    n = 1
    array_min = []
    step = (len(array_copy))
    while n < step / 2:
        x = min(array_copy)
        for i in array_copy:
            if i == x:
                num_min = i
                array_copy.remove(i)
                array_min.append(num_min)
        n += 1
    medium_array = min(array_copy)
    array_copy.remove(medium_array)

    print('Меньшая половина данного массива: {}'.format(array_min))
    print('Большая половина данного массива: {}'.format(array_copy))
    print('Медиана данного массива: {}'.format(medium_array))


medium(array_3)
