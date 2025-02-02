'''
def f(n):
    if n < 3:
        return n + 3
    if n % 3 == 0:
        return (n + 2) * f(n - 4)
    return n + f(n - 1) + 2 * f(n - 2)

print(f(20))
'''

'''
from functools import lru_cache
@lru_cache(None)

def f(n):
    if n == 1:
        return 1
    return 2 * f(n - 1) + g(n - 1) - 2 * n


def g(n):
    if n == 1:
        return 1
    return f(n - 1) + 2 * g(n - 1) + n

for i in range(1, 50):
    if f(i) == 597719:
        print(i)
'''

'''
def f(n):
    if n < 11:
        return n
    return n + f(n - 1)

print(f(2024) - f(2021))
'''

print((2024 + 10)/2*2015 - (2021 + 10)/2*2012)