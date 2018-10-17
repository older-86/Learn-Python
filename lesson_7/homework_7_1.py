# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный
# и отсортированный массивы.

print('Решение задачи №1')

import random

volume = 10
array_1 = [random.randint(-100, 100) for _ in range(volume)]
print('Исходный массив: {}'.format(array_1))



def sort_array(array):
    n = 1
    while n <= len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    print('Отсортированный: {}'.format(array))


sort_array(array_1)

