"""
#2
print("W Y Z X F")
for w in range(2):
    for y in range(2):
        for z in range(2):
            for x in range(2):
                F = ((x and y and (not z)) == (y or z or (not w)))
                if F == 1:
                    print(w, y, z, x, F)

print(3*(4**5))
"""

"""#4
s = 4 * 343**5 + 6 * 49**8 - 50
x = ''
while s != 0:
    x += str(s % 7)
    s = s // 7
x += str(s)
x = x[::-1]
#print(x)
print(x.count('6'))"""

"""#6
def f(n):
    if n >= 2000:
        return 2000
    if n < 2000 and n % 2 != 0:
        return n * f(n + 1)
    if n < 2000 and n % 2 == 0:
        return n * (f(n + 1) // 2)
print(f(1998)//f(2001))
"""

"""#2
s = '9' * 127

while '333' in s or '999' in s:
    s = s.replace('333', '9', 1)
    s = s.replace('999', '3', 1)

print(s)"""


#1
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w <= (not(x))) == (z <= y)) and (y or w):
                    print(x, y, z, w)

"""
"""
#2
print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w or (not(x))) and (w == (not(y))) and (w <= z)
                if F == 1:
                    print(x, y, z, w, F)       
"""

#1
'''
def D(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        #if D(90, A) and ((not(D(x, A))) <= (D(x, 15) <= (not(D(x, 20))))):
        if D(90, A) and (D(x, A) or (not(D(x, 15)) or not(D(x, 20)))):
            k += 1
    if k == 1000:
        print(A)
'''
"""
#2
def D(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if D(A, 40) and (not(D(780, x)) or (D(A, x) or not(D(180, x)))):
            k += 1
    if k == 1000:
        print(A)
        break
"""
#3
"""
for A in range(1, 300):
    k = 0
    for x in range(1, 301):
        for y in range(1, 301):
            if ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9)):
                k += 1
    if k == 300 * 300:
        print(A)
"""

#4
"""
count = 0
for A in range(1, 300):
    k = 0
    for x in range(1, 301):
        for y in range(1, 301):
            if ((x < A) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= A)):
                k += 1
    if k == 300*300:
        count += 1
print(count)
"""

'''
def F(a, b, x):
    if a <= x <= b:
        return True
    return False


d = 10**10

for a in range(1, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            if (F(4, 15, x) and F(12, 20, x)) <= F(a, b, x):
                k += 1

        if k == 198:
            d = min(d, b-a)

print(d) #3
'''

'''
def F(a, b, x):
    if a <= x <= b:
        return True
    return False


d = -10**10

for a in range(1, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            if (F(a, b, x) <= F(10, 29, x)) or F(13, 18, x):
                k += 1

        if k == 198:
            d = max(d, b-a)

print(d) #19
'''

'''
def F(a, b, x):
    if a <= x < b:
        return True
    return False


d = -10**10

for a in range(1, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            #if (F(5, 30, x) == F(14, 23, x)) <= (not (F(a, b, x))):
            if not (F(14, 23, x) == (F(5, 30, x))) or (not (F(a, b, x))):
                k += 1

        if k == 198:
            d = max(d, b-a)

print(d)
'''

'''
def DEL(n, m):
    if n % m == 0:
        return True
    return False


for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        #if DEL(120, A) and (DEL(x, A) or ((not (DEL(x, 18))) or not(DEL(x, 24)))):
        if DEL(120, A) and ((not (DEL(x, A))) <= ((DEL(x, 18)) or (not (DEL(x, 24))))):
            k += 1
    if k == 1000:
        print(A) #24
'''
'''
def F(a, b, x):
    if a <= x <= b:
        return True
    return False


d = -10**10

for a in range(1, 101):
    for b in range(1, 101):
        k = 0
        for i in range(2, 200):
            x = i/2
            if (F(a, b, x) <= F(2, 10, x)) or F(6, 14, x):
                k += 1
        if k == 198:
            d = max(d, b-a)

print(d) #12
'''
'''
def F(a, b, x):
    if a <= x <= b:
        return True
    return False


d = 10**10

for a in range(1, 101):
    for b in range(1, 101):
        k = 0
        for i in range(2, 200):
            x = i/2
            if (F(a, b, x) or F(10, 40, x)) or (F(5, 15, x) <= F(35, 50, x)):
                k += 1
        if k == 198:
            d = min(d, b-a)
print(d) #5
'''
'''
for A in range(0, 1000):
    k = 0
    for x in range(0, 1000):
        if (x & 25 != 0) <= ((x & 19 == 0) <= (x & A != 0)):
            k += 1
    if k == 1000:
        print(A)
        break
'''

#№5
'''
#4
for i in range(1, 1000):
    s = format(i, 'b')
    s += str(s.count("1") % 2)
    s += str(s.count("1") % 2)
    r = int(s, 2)

    if r > 83:
        print(r)
        break
'''

'''
#5
for i in range(1, 1000):
    s = format(i, 'b')
    if s.count('1') % 2 != 0:
        s += '11'
    else:
        s += '00'
    r = int(s, 2)

    if r > 114:
        print(r)
        break
'''

'''
#6
for i in range(1, 1000):
    s = format(i, 'b')
    if i % 2 == 0:
        s += '01'
    else:
        s += '10'

    r = int(s, 2)
    if r > 102:
        print(r)
        break
'''

'''
for i in range(1, 1000):
    s = format(i, 'b')
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)

    r = int(s, 2)
    if r > 97:
        print(r)
        break
'''
'''
for i in range(1, 1500):
    n = format(i, 'b')
    n1 = n[:-1]
    if i % 2 != 0:
        n1 += '10'
    if i % 2 == 0:
        n1 += '01'

    r = int(n1, 2)
    if r == 2017:
        print(i)
'''
'''
for i in range(1, 1000):
    s = format(i, 'b')
    s += str((s.count('1')) % 2)
    s += str((s.count('1')) % 2)

    r = int(s, 2)
    if r > 85:
        print(i)
        break
'''
'''
for i in range(100, 1000):
    s1 = int((str(i))[0]) + int((str(i))[1])
    s2 = int((str(i))[1]) + int((str(i))[2])
    #print(i, s1, s2)
    if s1 > s2:
        s = str(s2) + str(s1)
    else:
        s = str(s1) + str(s2)

    if int(s) == 1115:
        print(i)
        break
'''
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) == (z <= w)) or (x and w)
                if not F:
                    print(x, y, z, w, F)'''
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and not(y)) or (y == z) or not(w)
                if not F:
                    print(x, y, z, w, F)'''
'''
for i in range(1000, 10000):
    s = str(i)
    s1 = int(s[0]) + int(s[1])
    s2 = int(s[2]) + int(s[3])
    b = str(max(s1, s2))
    m = str(min(s1, s2))
    r = int(b + m)
    if r == 1311:
        print(i)
        break
'''
'''
for i in range(10000, 100000):
    s = str(i)
    s1 = int(s[0]) + int(s[2]) + int(s[4])
    s2 = int(s[1]) + int(s[3])
    b = str(max(s1, s2))
    m = str(min(s1, s2))
    r = int(m + b)
    if r == 723:
        print(i)
        break
'''