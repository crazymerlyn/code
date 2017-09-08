from utils import is_square, memoized
from fractions import gcd

@memoized
def s_factors(n):
    s = 0
    i = 1

    while i * i <= n:
        s += i * (n / i)
        i += 1
    i -= 1
    j = 1

    while n // (j+1) >= i:
        l = n / (j + 1)
        h = n / j
        s += j * (l + h + 1) * (h - l) // 2
        j += 1
    return s

s = 0
limit = 10 ** 8

for i in xrange(1, limit+1):
    s += i * (limit // i)

for a in xrange(1, int(limit ** 0.5) + 1):
    for b in xrange(1, min(a, int((limit - a * a) ** 0.5)) + 1):
        if gcd(a, b) > 1: continue
        n = a*a + b*b
        val = 2 * a if a == b else 2 * (a + b)
        x = limit // n
        s += val * s_factors(x)


print s

