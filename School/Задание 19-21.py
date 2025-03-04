"""from math import ceil


def g(s1, s2, h):
    if ((s1 + s2) <= 108) and h == 3:
        return True
    if ((s1 + s2) <= 108) and h != 3:
        return False
    if ((s1 + s2) > 108) and h == 3:
        return False

    if h % 2 == 0:  # Петя
        return g(s1 - 2, s2, h + 1) or g(s1, s2 - 2, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2), h + 1)
    else:  # Ваня
        return g(s1 - 2, s2, h + 1) or g(s1, s2 - 2, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2), h + 1)


for s2 in range(49, 1000):
    if g(60, s2, 1):
        print(s2)  # 192"""