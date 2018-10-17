# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

# Урок №1 задача №1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import sys

print('Урок №1. Решение задачи №1')

num = input('введите трехзначное число: ')

x = int(num[0])
y = int(num[1])
z = int(num[2])
sum_num = x + y + z
multiplication = x * y * z
print('сумма цифр трехзначного числа =', sum_num)
print('произведение цифр трехзначного числа =', multiplication)

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)


show_size(sum_num)

#type = <class 'int'>, size = 28, object = 16