'''
from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a + b >= 68:
        return 0
    t = [f(a+2, b), f(a, b+2), f(a*3, b), f(a, b*3)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n)+1
    else:
        return -max(t)


for i in range(1, 60):
    if f(8, i) == 5:
        print(i)'''
'''
#№ 11283 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a + b >= 342:
        return 0
    t = [f(a+2, b), f(a, b+2), f(a*5, b), f(a, b*5)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n)+1
    else:
        return -max(t)

s = []

for i in range(2, 326):
    if f(11, i) == 1:
        s.append(i)
print(min(s)/5)
'''

'''
#№ 11283 (Уровень: Базовый)
def f(s,s2, m):
    if s + s2 >= 342: return m%2==0
    if m == 0: return 0
    h = [f(s+2, s2, m-1), f(s*5, s2, m-1), f(s, s2+2, m-1), f(s, s2*5, m-1)]
    return any(h) if m%2!=0 else all(h) # меняем all на any в 19 задаче
print(19, min(s for s in range(1, 326) if f(11,s, 2)))
print(20, [s for s in range(1, 326) if not f(11,s, 1) and f(11,s, 3)][:2])
print(21, min(s for s in range(1, 326) if not f(11,s, 2) and f(11,s, 4)))
'''


