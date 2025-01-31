"""КИМ № 25057665
БР № 2832503195017"""
# https://kompege.ru/variant?kim=25057665

# 17 17680
"""s = [int(x) for x in open('files/17_17680.txt')]

min41 = float('inf')
for x in s:
    if x > 0 and x % 41 == 0:
        min41 = (min(min41, x))

ans = []
for i in range(len(s) - 1):
    if s[i] != s[i + 1] and abs(s[i] - s[i + 1]) % min41 == 0:
        ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))  # 10 92404"""

# 24 17685
# Wrong!
"""Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной последовательности, являющейся корректным
арифметическим выражением с целыми неотрицательными числами (без знака), значение которого равно нулю. В этом выражении никакие два знака арифметических операций не стоят рядом, порядок
действий определяется по правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули.
В ответе укажите количество символов."""

"""s = open('files/24_17685.txt').readline()
for n in '23456789': s = s.replace(n, '1')
while '**' in s: s = s.replace('**', ' ')
while '+*' in s: s = s.replace('+*', ' ')
while '*+' in s: s = s.replace('*+', ' ')
while '++' in s: s = s.replace('++', ' ')

m = ''
for c in s.split():
    if len(c) > len(m):
        for i in range(len(c)-1):
            if c[i] + c[i+1] not in ('01', '00'):
                sub = ''
                for j in range(i, len(c)):
                    sub += c[j]
                    if sub[0] not in '*+' and sub[-1] not in '*+':
                        if eval(sub) == 0:
                            m = max(m, sub, key=len)
print(len(m), m)  # 169"""
# 9 17672
"""c = 0
f = open('files/9_17672.txt')
for s in f:
    a = sorted(int(x) for x in s.split())
    if a[-1] + a[0] < a[1] + a[2]:
        c += 1
print(c)  # 9997"""

# 25 17686

"""def div(x):
    s = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            if i % 10 == 7 and i != 7 and i != x:
                s.add(i)
            if (x / i) % 10 == 7 and (x / i) != 7 and (x / i) != x:
                s.add(x // i)
    if len(s) > 0:
        return min(s)
    return False

c = 0
for i in range(700_000, 701_000):
    if div(i):
        if c < 5:
            print(i, div(i))
            c += 1"""


# 23 17684

"""def f(x, end):
    if x == end:
        return True
    if x < end:
        return False
    if x > end:
        return f(x - 2, end) + f(x // 2, end)


print(f(38, 10) * f(10, 2))  # 30"""
