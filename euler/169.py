from math import log
from utils import memoized

@memoized
def count(n, d=None):
    if d == 0: return n == 0
    if n < 0: return 0
    if n <= 1: return 1
    if d is None:
        d = 2**int(log(n, 2))
    if n > 4*d - 2: return 0

    res = count(n, d/2) + count(n-d, d/2) + count(n-2*d, d/2)
    return res

print count(10**25)

