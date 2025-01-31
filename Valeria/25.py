"""def div(x):
    m = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            m.add(i)
            m.add(x // i)
    return m


for i in range(700_000, 750_000):
    if len(div(i)) > 1:
        m = max(div(i)) + min(div(i))
        if m % 10 == 8:
            print(i, m)"""
# 700005 233338
# 700007 100008
# 700012 350008
# 700015 140008
# 700031 24168

"""from fnmatch import *

for i in range(141, 10**8, 141):
    if fnmatch(str(i), '1234*7'):
        print(i, i // 141)"""
# 1234737 8757
# 12341307 87527
# 12342717 87537
# 12344127 87547
# 12345537 87557
# 12346947 87567
# 12348357 87577
# 12349767 87587

"""from fnmatch import *

for i in range(2023, 10**10, 2023):
    if fnmatch(str(i), '1?2139*4'):
        print(i, i // 2023)"""

# 162139404 80148
# 1321399324 653188
# 1421396214 702618
# 1521393104 752048


"""def div(x):
    m = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            m.add(i)
            m.add(x // i)
    return sorted(m)


for i in range(174457, 174506):
    m = div(i)
    if len(m) == 2:
        print(m)"""


# [3, 58153]
# [7, 24923]
# [59, 2957]
# [13, 13421]
# [149, 1171]
# [5, 34897]
# [211, 827]
# [2, 87251]


"""def div(x):
    m = {1}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            m.add(i)
            m.add(x // i)
    return sorted(m)


for i in range(770_000, 1, -1):
    a = sum(div(i)) // len(div(i))
    if a % 100 == 12:
        print(i, a)"""
# 7769995 25612
# 769923 18312
# 769916 35712
# 769700 27112
# 769583 2912


"""from fnmatch import *

for i in range(2024, 10**10, 2024):
    if fnmatch(str(i), '3?6906*4'):
        print(i)"""
# 3969064
# 336906944
# 3069064064
# 3169069904
# 3269065624
# 3369061344
# 3469067184
# 3569062904
# 3669068744
# 3769064464
# 3869060184
# 3969066024

"""def div(x):
    m = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            m.add(i)
            m.add(x // i)
    return sorted(m)


for i in range(174457, 174506):
    m = div(i)
    if len(m) == 2:
        print(m)"""

# [3, 58153]
# [7, 24923]
# [59, 2957]
# [13, 13421]
# [149, 1171]
# [5, 34897]
# [211, 827]
# [2, 87251]

