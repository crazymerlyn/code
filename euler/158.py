from math import factorial

def comb(n, r):
    if r > n: return 0
    return factorial(n) / factorial(n - r) / factorial(r)

def p(n):
    return comb(26, n) * (2 ** n - n - 1)

print max(p(n) for n in range(1, 27))

