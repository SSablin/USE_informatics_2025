# 19-21 №22232
from functools import lru_cache


@lru_cache(None)
def game(a):
    if a <= 24: return 'END'
    h = [game(a - 3)]
    if a % 2 == 0:
        h.append(game(a // 2))
    else:
        h.append(game((a + 3) // 2))
    if 'END' in h: return 'W1'
    if set(h) == {'W1'}: return 'L1'
    if 'L1' in h: return 'W2'
    if set(h) in [{'W2'}, {'W1', 'W2'}]: return 'L12'


print(min(s for s in range(25, 1000) if game(s) == 'L1'))  # 47
print([s for s in range(25, 1000) if game(s) == 'W2'])  # 50 52
print(min(s for s in range(25, 1000) if game(s) == 'L12'))  # 53
