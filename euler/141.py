from fractions import gcd
from utils import is_square

limit = 10 ** 12
res = set()

for a in range(2, 10 ** 4):
    for b in range(1, min(a, limit / a ** 3)):
        if gcd(a, b) > 1: continue
        for c in range(1, int((limit // a ** 3 // b) ** 0.5)):
            n = a**3 * b * c * c + c * b ** 2
            if is_square(n):
                res.add(n)

print sum(res)
