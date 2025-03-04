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