from math import factorial as fac, log, exp
from fractions import gcd
from decimal import Decimal

n = 20000
limit = 10 ** 6

factorial = [i for i in range(limit+1)]
for i in range(1, limit+1):
    factorial[i] = Decimal(log(factorial[i], 10)) + factorial[i-1]

res = Decimal(0)
for q in range(n//2 + 1):
    p = n - 2 * q
    f = factorial[n] + factorial[limit] -factorial[p] - factorial[q] - factorial[limit - p - q] - Decimal(log(limit, 10) * n) - Decimal(log(2, 10) * q)
    res += Decimal(10) ** Decimal(f)

print(Decimal(1) - res)
