# №2
"""print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not(y)) <= (z == w)) and ((z <= x) == w)
                if f == True:
                    print(x, y, z, w, f)"""

# №12
"""s = '1' + '9' * 98
while '19' in s or '299' in s or '3999' in s:
    s = s.replace('19', '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print(s) #29
"""
# №14
"""
s = 4**12 + 2**32 - 16
s2 = ''
while s >= 2:
    s2 += str(s % 2)
    s = s // 2
s2 += str(s)
s2 = s2[::-1]
print((s2)) #1а
#21
"""
# №16
# EXEL

# 13
# 183.253.231.64
# Г Б А В

"""
P = range(4, 15)
Q = range(12, 20)
A = [int(i) for i in range (1, 15)]
for x in range(100):
    if (((x in P) and ((x in Q))) <= (x in A)):
        A = A[1:]
    else:
        print(len(A))"""
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(x) or y or z) and (x or not(z) or not(w))
                if F == 0:
                    print(x,y,z,w)
"""
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(z)) and (not(x == y))) <= (not(y or w))
                if F == 0:
                    print(x, y, z, w)

"""

# 15
"""
def DEL(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if (not(DEL(x, 40)) and not(DEL(x, 64))) or DEL(x, A):
            k = k + 1
    if k == 1000:
        print(A)

def DEL(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if DEL(x, A) or (not(DEL(x, 6)) or not(DEL(x, 9))):
            k = k + 1
    if k == 1000:
        print(A)
"""
"""
def DEL(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if (DEL(x, A)) or (not(DEL(x, 6)) or not(DEL(x, 4))):
            k += 1
    if k == 1000:
        print(A)
"""
"""
k = 0
for x in range(1, 1000):
    if not(x**2 >= 9) or not((x < 7) or (x >= 10)):
        k += 1
print(k)
"""
"""
for A in range(0, 1000):
    k = 0
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (x >= A) or (y >= A) or (x * y <= 205):
                k += 1
        if k == 1000 * 1000:
            print(A)
"""

"""
#15
def F(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False

d = 10**10

for a in range(0, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            if not((F(10,15,x) or F(20,27,x))) or F(a,b,x):
                k += 1

        if k == 198:
            d = min(d, b-a)
print(d)
"""
'''
def F(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False

d = -10**10

for a in range(0, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            #if (not(F(a,b,x)) or F(43,49,x)) or F(44,53,x):
            if (F(a, b, x)) <= F(43, 49, x) or F(44, 53, x):
                k += 1

        if k == 198:
            d = max(d, b-a)
print(d)
'''
'''
def F(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False

d = 10**10

for a in range(0, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            if (F(a, b, x) or (F(14, 20, x) == F(15, 27, x))):
                k += 1

        if k == 198:
            d = min(d, b-a)
print(d)
'''

# поразрядная коньюнкция
'''
for A in range(0, 1000):
    k = 0
    for x in range(0, 1000):
        if ((x & A == 0) and (((x & 35 == 0) or ((x & 52 != 0)):
            k += 1
    if k == 1000:
        print(A)
        '''
'''
for A in range(0, 1000):
    k = 0
    for x in range(0, 1000):
        if (x & 56 != 0) <= ((x & 48 == 0) <= (x & A != 0)):
            k += 1
    if k == 1000:
        print(A)
        break

'''

# № 15
'''
for i in range(1, 1000):
    s = format(i, "b") #переводим в двоичный вид
    s += str(s.count("1") % 2)
    s += str(s.count("1") % 2)
    r = int(s, 2)
    if r > 42:
        print(r)
        break
'''
'''
for i in range(1, 1000):
    s = format(i, "b") #переводим в двоичный вид
    if i % 2 == 0:
        s += '00'
    else:
        s += '11'
        
    r = int(s, 2)
    if r > 130:
        print(i)
        break
'''
'''
for i in range(1, 1000):
    s = format(i, 'b')
    s = s.replace('0', '*')
    s = s.replace('1', '10')
    s = s.replace('*', '01')
    r = int(s, 2)
    if r % 2 != 0 and r < 256:
        print(r)
'''
'''
for i in range(1, 1000):
    a = i
    a -= a % 4
    s = format(a, 'b')
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    r = int(s, 2)
    if r < 47:
        print(i)
'''
'''
for i in range(1, 1000):
    s = format(i, 'b')
    if s.count('1') % 2 == 0:
        s += '0'
        s = '10' + s[2:]
    else:
        s += '1'
        s = '11' + s[2:]
    r = int(s, 2)
    if r > 40:
        print(i)
        break
'''
'''
for i in range(3, 1000):
    s = format(i, 'b')
    s += s[-2]
    s += s[1]
    r = int(s, 2)
    if r > 170:
        print(i)
        break
'''
'''
for i in range(1, 256):
    s = format(i, 'b')
    while len(s) < 8:
        s = '0' +s
    s = s[:-1]
    s = s[::-1]

    r = int(s, 2)
    if i < 100:
        if i == r:
            print(r)
'''
'''
for i in range(1, 1000):
    s = format(i, 'b')
    if s.count('1') % 2 == 0:
        s += '0'
        s = '1' + s[2:]
    else:
        s += '1'
        s = '11' + s[2:]

    r = int(s, 2)
    if r > 49:
        print(i, r)
'''
'''
def F(a):
    s = ''
    while a > 0:
        s += str(a % 3)
        a = a // 3
    return s[::-1]

d = 10**10
for i in range(1, 1000):
    s = F(i)
    if i % 3 == 0:
        s += s[-2] + s[-1]
    else:
        s += F((i % 3) * 5)

    r = int(s, 3)
    if r > 133:
        d = min(d, r)
print(d)
'''
'''
for i in range(1000, 10000):
    s = str(i)
    a = int(s[0]) * int(s[1])
    b = int(s[2]) * int(s[3])
    if a > b:
        r = str(a) + str(b)
    else:
        r = str(b) + str(a)

    if r == '124':
        print(i)
'''

'''
max = -10**10
for i in range(0, 12):
    s = format(i, 'b')
    if int(s) % 2 == 0:
        s += '10'
    else:
        s = '1' + s + '01'

    otv = int(s, 2)
    if otv > max:
        max = otv
print(otv)
'''
'''
min = 10**10
for i in range(1, 1000):
    s = format(i, 'b')
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'

    r = int(s, 2)

    if r > 123 and r < min:
        min = r
print(min)'''

'''
for i in range(100, 1000):
    s = str(i)
    s1 = int(s[0]) + int(s[1])
    s2 = int(s[1]) + int(s[2])
    q = str(min(s1, s2))
    w = str(max(s1, s2))
    a = q + w
    if a == '1115':
        print(i)
        break
'''
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(z) and not(x == y)) <= (not(y or w))
                if not F:
                    print(x, y, z, w)
'''
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= y) <= x) or not(z)
                if not F:
                    print(x, y, z, w)
'''

'''k = 0
for x in range(1, 1000000):
    if not (x**2 >= 9) or not ((x < 7) or (x >= 10)):
        k += 1
print(k)

'''
'''
def F(a, b, x):
    if a <= x <= b:
        return True
    return False

m = 10**10
for a in range(1, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            if not (not ((F(10, 15, x) or F(20, 27, x))) <= F(a, b, x)):
                k += 1

        if k == 198:
            m = min(m, b-a)
print(m)
'''
'''
m = -10**10
for A in range(0, 300):
    k = 0
    for x in range(1, 301):
        for y in range(1, 301):
           if (x >= A) or (y >= A) or (x * y <= 205):
                k += 1

    if k == 300*300:
            print(A)'''

'''
def DEL(n, m):
    if n % m == 0:
        return True
    return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        #if (not DEL(x, A) <= (DEL(x, 6) <= (not DEL(x, 9)))):
        if DEL(x, A) or (not (DEL(x, 6))) or (not (DEL(x, 9))):
            k += 1

    if k == 1000:
        print(A)'''

'''
for A in range(0, 1000):
    k = 0
    for x in range(0, 1000):
        if (x & 51 != 0) <= ((x & A == 0) <= (x & 25 != 0)):
            k += 1

    if k == 1000:
        print(A)
        break'''

# №7
# print((48000 * 34 * 2540 * 2 + 110 * 1024 * 8 * 13) / 314572800)
# print((280 * 96468992)/(1024*960*11))
# print((280*1966080)/(39*1280*1024))
# print((16*4800*2*90)/(3200))

# 8
'''k = 0
for x1 in 'АБВГ':
    for x2 in 'АБВГ':
        for x3 in 'АБВГ':
            for x4 in 'АБВГ':
                for x5 in 'АБВГ':
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count('А') == 1:
                        k += 1
print(k)'''
'''
k = 0
bykv = 'ЕСАУЛ'
for x1 in bykv:
    for x2 in bykv:
        for x3 in bykv:
            for x4 in bykv:
                for x5 in bykv:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count(x1) == 1 and  \
                            s.count(x2) == 1 and \
                            s.count(x3) == 1 and \
                            s.count(x4) == 1 and \
                            s.count(x5) == 1:
                        if s.count('ЕА') == 0 and \
                                s.count('АЕ') == 0 and \
                                s.count('ЕУ') == 0 and \
                                s.count('УЕ') == 0 and \
                                s.count('АУ') == 0 and \
                                s.count('УА') == 0:
                                k += 1

print(k)'''

'''
k = 0
b = 'БЕЛКА'
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                if s.count('Б') == 1:
                    k += 1
print(k)'''

'''
b = 'КАТЕР'
k = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if s[0] == 'Р' and s[-1] == 'К':
                            k += 1
print(k)'''
'''
b = 'КБЛА'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if s.count('К') == 1 and \
                            s.count('Б') == 1 and \
                            s.count('Л') == 1 and \
                            s.count('А') == 3:
                            if s.count('АА') == 0:
                                    c += 1
print(c)'''
'''
b = 'ЕГЭ'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            if x1 == 'Э' or x1 == 'Е':
                s = x1 + x2 + x3
                c += 1

print(c)'''
'''
b = 'СОЛВЕЙ'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if x1 != 'Й' and x6 != 'Й' and s.count('ЙЕ') == 0 and s.count('ЕЙ') == 0 and s.count('Й') <= 1:
                            c += 1

print(c)'''
'''
b = '01234567'
c = 0
for x1 in '1234567':
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        for x7 in b:
                            s = x1 + x2 + x3 + x4 +x5 + x6 + x7
                            if s.count(x1) == 1 and s.count(x2) == 1 and s.count(x3) == 1 and s.count(x4) == 1 and s.count(x5) == 1 and s.count(x6) == 1 and s.count(x7) == 1:
                                if int(x1) % 2 == 0 and int(x2) % 2 != 0 and int(x3) % 2 == 0 and int(x4) % 2 != 0 and int(x5) % 2 == 0 and int(x6) % 2 != 0 and int(x7) % 2 == 0:
                                    c += 1
                                if int(x1) % 2 != 0 and int(x2) % 2 == 0 and int(x3) % 2 != 0 and int(x4) % 2 == 0 and int(x5) % 2 != 0 and int(x6) % 2 == 0 and int(x7) % 2 != 0:
                                    c += 1

                                    
print(c)'''
'''
b = 'АЕИО'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                c += 1
                if c == 248:
                    print(s)'''
'''b = 'ИКНОТ'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                c += 1
                if x1 == 'О':
                    break
print(c)'''
