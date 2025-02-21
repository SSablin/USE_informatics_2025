"""№ 20189 (Уровень: Средний)
(М. Попков) Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел.
Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
– в строке ровно два числа повторяются дважды, остальные числа различны;
– произведение двух наименьших чисел больше суммы пяти оставшихся."""

"""c = 0
for s in open('files/9.17_20189.txt'):
    a = sorted([int(x) for x in s.split()])
    povtor = [a.count(x) for x in a]
    if povtor.count(1) == 3 and povtor.count(2) == 4:
        if a[0] * a[1] > sum(a[2:]):
            c += 1
print(c)  # 113"""

"""№ 20190 (Уровень: Базовый)
(М. Попков) Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел. 
Определите количество строк таблицы, в которых хотя бы три числа 
могут образовывать геометрическую прогрессию с отличным от единицы знаменателем прогрессии.
В ответе запишите только число."""

"""from itertools import permutations


def geomprogression(a):
    for x in permutations(a, r=3):
        x = sorted(x)
        if (x[2] / x[1]) == (x[1] / x[0]):
            if (x[2] / x[1]) != 1:
                print(x)
                return True
    return False


c = 0
for s in open('files/9.7_20190.txt'):
    a = sorted([int(x) for x in s.split()], reverse=True)
    if geomprogression(a):
        print(a)
        c += 1
print(c)  # 56"""

"""
№ 19878 (Уровень: Средний)
(М. Попков) Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел. 
Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
– в строке ровно одно число повторяется трижды, остальные числа различны;
– среднее арифметическое неповторяющихся чисел не больше повторяющегося числа.
В ответе запишите только число."""
"""c = 0
for s in open('files/9.19_19878.txt'):
    a = sorted([int(x) for x in s.split()])
    povtor = [a.count(x) for x in a]
    if povtor.count(3) == 3 and povtor.count(1) == 4:
        pov = set(x for x in a if a.count(x) == 3)
        nepov = [x for x in a if a.count(x) == 1]
        if sum(nepov) / len(nepov) <= sum(pov):
            c += 1
print(c)  # 58"""
"""c = 0
for s in open('files/9.19_19878.txt'):
    a = sorted([int(x) for x in s.split()])
    povtor = [a.count(x) for x in a]
    if povtor.count(3) == 3 and povtor.count(1) == 4:
        nepov = []
        pov = 0
        for x in a:
            if a.count(x) == 1:
                nepov.append(x)
            else:
                pov = x
        if sum(nepov) / len(nepov) <= pov:
            c += 1
print(c)  # 58"""
