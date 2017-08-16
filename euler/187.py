from utils import primes
from bisect import bisect_right

limit = 10**8

ps = list(primes(limit))

res = 0
for i, p in enumerate(ps):
    if p * p > limit: break
    x = limit / p
    if limit % p:
        j = bisect_right(ps, x)
    else:
        j = bisect_right(ps, x-1)
    res += j - i

print res
