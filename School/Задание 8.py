# № 17549 Основная волна 08.06.24 (Уровень: Базовый)
"""c = 0
from itertools import product
for i in product(sorted('ФОКУС'), repeat=5):
    s = ''.join(i)
    c += 1
    if s.count('Ф') == 0 and s.count('У')== 2:
        print(c)  # 2313
"""

# № 17521 Основная волна 07.06.24 (Уровень: Базовый)

"""from itertools import product
from string import *
c = 0
for i in product(digits[:8], repeat=5):
    s = ''.join(i)
    if s[0] not in '01357' and s[-1] not in '26' and s.count('7') <= 2:
        print(s)
        c += 1
print(c)"""

# № 17627 Основная волна 19.06.24 (Уровень: Базовый)

"""from itertools import *
from string import *
c = 0
for x in product((digits+ascii_uppercase)[:15], repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('8') == 1 and (s.count('A') + s.count('B') + s.count('C') + s.count('D') + s.count('E')) >= 2:
        c += 1
print(c)"""

# № 17862 Демоверсия 2025 (Уровень: Базовый)
"""from itertools import *
c = 0
for x in product('012345678AAA', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('7') == 1 and s.count('A') <= 3:
        c += 1
print(c)  # 67476"""

# № 18972 (Уровень: Средний)
"""from itertools import product

k = 0
for i in product([i for i in range(25)], repeat=4):
    if i[0] != 0 and sum(j % 2 == 0 for j in i) == 1 and sum(1 for j in i if j > 15) <= 2:
        k += 1
print(k)"""

# № 18973 (Уровень: Средний)
"""from itertools import product
c = 0
for i in product([i for i in range(25)], repeat=4):
    if i[0] != 0 and sum(j % 2 == 0 for j in i) >= 1 and sum(j > 15 for j in i) > 2:
        c += 1
print(c)  # 50184"""

# 8 18976
"""from itertools import product

alf = [int(x) for x in range(20)]
c = 0
for x in product(alf, repeat=5):
    if x[0] != 0:
        if x[0] + x[-1] == 26:
            if "".join(str(x % 2) for x in x).count('11') == 0 and \
                    "".join(str(x % 2) for x in x).count('00') == 0:
                c += 1
                print(x, c)  # 13000"""

"""from itertools import product

c = 0
for x in product(sorted('СИНЕРГЯ'), repeat=6):
    c += 1
    s = ''.join(x)
    if s.count('ГИРЯ') > 0:
        print(c, s)  # 115381"""

# 8 №18258
"""from itertools import product
c = 0
for x in product((str(x) for x in range(12)), repeat=6):
    if x[0] != '0' and sum(1 for i in x if int(i) % 2 == 0) == sum(1 for i in x if int(i) % 2 != 0) and x.count('11') == 1:
        c += 1
        print(c, x)"""

# №21894
from itertools import product

c = 0
for i in product('0123456789', repeat=4):
    s = ''.join(i)
    if s[0] != '0':
        # if all(s.count(x) == 1 for x in s):
        if len(set(s)) == len(s):
            s1 = s
            for ch in '02468': s1 = s1.replace(ch, '0')
            for nch in '13579': s1 = s1.replace(nch, '1')
            if s1.count('11') == 0 and s1.count('00') == 0:
                c += 1
                print(s, c)  # 720

