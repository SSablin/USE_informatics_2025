# №19637
"""
from itertools import *


def f(x, y, w, z):
    return (z <= x) and ((x and (y == (not z))) <= w)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = {(a1, 1, 1, a2), (0, 0, a3, a4), (a5, 0, 0, 0)}
    for p in permutations('xywz'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            print(*p)  # z w y x

#     zip(p, r) создает пары из переменных и их значений для текущей строки таблицы.
#
#     dict(zip(p, r)) создает словарь, где ключи — это переменные,
#     а значения — соответствующие им значения из строки таблицы.
#
#     f(**dict(zip(p, r))) вызывает функцию ff с аргументами, соответствующими текущей строке таблицы.
#
#     [f(**dict(zip(p, r))) for r in table] создает список результатов функции ff для всех строк таблицы.
#
#     Мы проверяем, что этот список равен [0, 0, 0], что соответствует заданным значениям функции FF в таблице.
"""
i = 12345
print((''.join(f'{x}*' for x in map(int, str(i))))[:-1])
print(eval((''.join(f'{x}*' for x in map(int, str(i))))[:-1]))