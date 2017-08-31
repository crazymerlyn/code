from utils import factorize
from math import e, ceil, log
from fractions import Fraction
from decimal import Decimal

limit = 10000
res = 0

for n in range(5, limit+1):
    a = int(n/e)
    b = int(ceil(n/e))

    k = max([a, b], key=lambda x: x * log(1.0*n/x))
    denom = Fraction(n, k).denominator

    if not all(p in (2, 5) for p,_ in factorize(denom)):
        res += n
    else:
        res -= n

print res

