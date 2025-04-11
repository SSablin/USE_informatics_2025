# № 18372 (Уровень: Базовый)

"""def d(n):
    m = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            m.add(i)
            m.add(n // i)
    return sum(m) // len(m)

c = 0
x = 770_000
while c < 5:
    x -= 1
    A = d(x)
    if A % 100 == 12:
        c += 1
        print(x, A)"""

# 769995 25612
# 769923 18312
# 769916 35712
# 769700 27112
# 769583 2912

"""def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        # if x % i == 0: d |= {i, x // i}
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for n in range(112_500_000, 112_550_000):
    d = div(n)
    if len(d) >= 2:
        m = d[-1] + d[-2]
        if m % 10000 == 1214:
            print(n)"""
# 112508413
# 112520369
# 112523549
# 112534952

# 25 шастин10
"""from fnmatch import fnmatch

for i in range(4321, 10**9, 4321):
    if fnmatch(str(i), '34*56?7'):
        if str(eval((''.join(f'{x}*' for x in map(int, str(i))))[:-1]))[-1] == '0':
            print(i, eval((''.join(f'{x}*' for x in map(int, str(i))))[:-1]))"""

"""№ 18192 (Уровень: Базовый)

(Д. Бахтиев) Напишите программу, которая перебирает целые числа, бо́льшие 1 000 000, 
в порядке возрастания и ищет среди них те, которые имеют ровно 3 простых делителя. 
В ответе запишите 5 наименьших таких чисел в порядке возрастания. 
Справа от каждого такого числа укажите его наибольший простой делитель"""

"""def d(n):
    m = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            m.add(i)
            m.add(n // i)
    return m


x = 1_000_000
count = 0
while count < 5:
    x += 1
    div = d(x)
    count_d = []
    for number in div:
        div_number = d(number)
        if len(div_number) == 0:
            count_d.append(number)
    if len(count_d) == 3:
        print(x, max(count_d))
        count += 1"""

# 25 №21422
"""c = 0
while c < 5:
    for x in range(1_125_000, 2_000_000):
        if c < 5:
            for i in range(1, x):
                if x % i == 0 and i % 10 == 7 and i != 7:
                    print(x, i)
                    c += 1
                    break
# 1125003 467
# 1125005 7
# 1125006 97
# 1125009 17
# 1125011 3187"""