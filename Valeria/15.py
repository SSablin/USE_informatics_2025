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

#15
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
"""print('p q r a f')
for p in range(2):
    for q in range(2):
        for r in range(2):
            for a in range(2):
                f = (((not a) <= (not p)) == (q <= r))
                if f:
                    print(p, q, r, a, f)"""

