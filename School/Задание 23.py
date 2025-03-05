# 20198
"""def f(s, e, a):
    if s == e and a < 3:
        return 1
    elif s > e + 3 or a == 3:
        return 0
    return f(s - 1, e, a + 1) + f(s + 5, e, 0) + f(s * 2, e, 0)


print(f(5, 34, 0))  # 21428"""

# №19883
"""def f(s, e):
    if s == e:
        return 1
    if s < e or s == 24:
        return 0
    if s > 9:
        return f(s - 1, e) + f(int(s ** 0.5), e) + f(s // 10, e)
    else:
        return f(s - 1, e) + f(int(s ** 0.5), e)


print(f(602, 7))  # 1393"""

# 23 №20198
"""def p(x, end, c):
    if x > end + 2:
        return 0
    if x == end:
        return 1
    else:
        if c <= 1:
            return p(x - 1, end, c + 1) + p(x + 5, end, 0) + p(x * 2, end, 0)
        else:
            return p(x + 5, end, 0) + p(x * 2, end, 0)


print(p(5, 34, 0))  # 21428"""

# Попков
# 23 №19883
"""def f(start, end):
    if start < end or start == 24:
        return 0
    elif start == end:
        return 1
    else:
        if start > 9:
            return f(start - 1, end) + f(int(start ** 0.5), end) + f(start // 10, end)
        else:
            return f(start - 1, end) + f(int(start ** 0.5), end)


print(f(602, 7))  # 1393"""


# Попков
# 23 №20198
"""def f(start, end, s):
    if start > end + 3 or 'AAA' in s:  # +2, с запасом +3
        return 0
    if start == end and 'AAA' not in s:
        return 1
    else:
        return f(start - 1, end, s + 'A') + f(start + 5, end, s + 'B') + f(start * 2, end, s + 'C')


print(f(5, 34, ''))  # 21428"""
