# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib
# или встроенную функцию hash()


print('Решение задачи №1')

import hashlib


def rabin_karp(s):
    array_str = []
    num_subs = 0
    for i in range(len(s) - 1):
        for j in range(len(s) - 1):
            # left = s[j:i+1]
            if (j) < (i + 1):
                h_sub_left = hashlib.sha1(s[j:i + 1].encode('utf-8')).hexdigest()
                # print('Подстрока слева: {}, ХЭШ - {}'.format(left, h_sub_left))
                array_str.append(h_sub_left)
                # right = s[i+1:]
                h_sub_right = hashlib.sha1(s[i + 1:j].encode('utf-8')).hexdigest()
                # print('Подстрока справа: {}, ХЭШ - {}'.format(right, h_sub_right))
                array_str.append(h_sub_right)

    num_set = set(array_str)
    for i in num_set:
        num_subs += 1
    return num_subs


s_1 = input('Введите строку: ')

pos = rabin_karp(s_1)

print(f'итог = {pos}')
