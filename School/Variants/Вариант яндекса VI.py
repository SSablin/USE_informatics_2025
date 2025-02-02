# 5
# https://education.yandex.ru/ege/task/f4f17581-c911-4ab0-9a72-a70827259b20

"""min_n = float('inf')
for n in range(1000, 10000):
    num = sorted(int(x) for x in str(n))
    if sum(num.count(x) for x in num) == 4:
        mm = num[-1] + num[0]
        el = num[1] * num[2]
        r = int(str(min(mm, el)) + str(max(mm, el)))
        if r > 85:
            print(n)  # 1089"""
# 6
# https://education.yandex.ru/ege/task/3d1c2b6c-075c-467b-b1ae-b9443f968900'
"""from turtle import *

tracer(0)
screensize(5000, 5000)

c = 30
lt(90)

rt(30)
fd(4 * c)
rt(330)

down()

fd(4 * c)
rt(90)
fd(7 * c)
rt(45)
fd(4 * (2 ** 0.5) * c)
rt(135)
fd(11 * c)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'green')
# 38
exitonclick()
update()"""

# 8
# https://education.yandex.ru/ege/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9
"""from itertools import product

def glasn(s):
    for i in range(len(s) - 2):
        if s[i + 1] in glas and s[i] in sogl and s[i + 2] in sogl:
            return False
    return True


glas = sorted('ИЕОА')
sogl = sorted('ГПРБЛ')
c = 0
for x in product((sorted(set('ГИПЕРБОЛА'))), repeat=6):
    s = ''.join(x)
    if s[0] not in glas and s[-1] not in glas and glasn(s):
        c += 1
        print(s, c)  # 68025"""

# 13
# https://education.yandex.ru/ege/task/c50813d8-cee9-4ee3-863d-030766ef86f9
"""from ipaddress import *

net = ip_network('212.192.32.96/255.255.255.224')
c = 0
for ip in net:
    b = f'{ip:b}'
    if b[-8:].count('111') == 0 and b[-8:].count('000') == 0:
        c += 1
print(c)  # 8"""


# 24
# https://education.yandex.ru/ege/task/01dfb7d5-1b71-470d-adf4-612e4adaaf7e
"""Текстовый файл состоит из символов латинского алфавита в нижнем регистре (a—z) и цифр (0-9).
Определите в прилагаемом файле максимальную длину подстроки (непрерывной подпоследовательности), 
которая состоит из повторяющегося слова "yandex". Последнее слово в цепочке может быть неполным. 
По правилам leet (1337) символ "a" может быть заменён на символ "4", а символ "e" — на символ "3".
Так, в строке "qyandqqyand3xy4q" есть две подходящие подстроки: "yand" и "yand3xy4"."""
"""
from string import ascii_lowercase

s = open('files/24_яндексVI.txt').readline().strip()


for n in '01256789': s = s.replace(n, ' ')
for n1 in '34': s = s.replace(n1+n1, ' ')
for w in ascii_lowercase:
    while w+w in s:
        s = s.replace(w+w, ' ')

m = ''
for c in s.split():
    for i in range(len(c) - 5):
        if s[i:i+7] == 'yandex' or s[i:i+7] == 'yand3x' or s[i:i+7] == 'y4ndex' or s[i:i+7] == 'y4nd3x':
            sub = c[i:i + 7]
            for j in range(i+7, len(s), 6):
                if s[i:i + 7] == 'yandex' or s[i:i + 7] == 'yand3x' or s[i:i + 7] == 'y4ndex' or s[i:i + 7] == 'y4nd3x':
                    sub += c[i:i+7]
                else:
                    sub += c[i:i+7]
                    m = max(m, sub, key=len)
                    break
print(m, len(m))"""
