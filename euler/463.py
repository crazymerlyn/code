from utils import memoized

@memoized
def f(n):
    if n == 1: return 1
    if n == 3: return 3
    if n % 2 == 0: return f(n // 2)
    if n % 4 == 1:
        return 2 * f(2 * n // 4 + 1) - f(n // 4)
    return 3 * f(n // 2) - 2 * f(n // 4)

@memoized
def s(n):
    if n < 4: return [0, 1, 2, 5][n]
    res = 0
    while n % 4 != 3:
        res += f(n)
        n -= 1
    return res + 6 * s(n // 2) - 8 * s(n // 4) - 1

print(s(3 ** 37))
