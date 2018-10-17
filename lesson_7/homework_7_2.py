# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
# отсортированный массивы.

print('Решение задачи №2')

import random

volume = 10
array_2 = [random.randrange(0, 50) for _ in range(volume)]
print('Исходный массив: {}'.format(array_2))


def sort_array(array):
    def group_array(array, left, medium, right):
        if left >= right: return None
        if medium < left or right < medium: return None
        x = left
        for j in range(medium + 1, right + 1):
            for i in range(x, j):
                if array[j] < array[i]:
                    r = array[j]
                    for k in range(j, i, -1):
                        array[k] = array[k - 1]
                    array[i] = r
                    x = i
                    break

    if len(array) < 2: return None
    k = 1
    while k < len(array):
        g = 0
        while g < len(array):
            z = g + k + k - 1
            r = z if z < len(array) else len(array) - 1
            group_array(array, g, g + k - 1, r)
            g += 2 * k
        k *= 2
    print('Отсортированный: {}'.format(array))


sort_array(array_2)
