from utils import primes
from math import log

def powers(l, limit):
    res = l
    while res <= limit:
        yield res
        res *= l

limit = 10 ** 7
ps = list(primes(limit/2))

res = 0
for lp in ps[::-1]:
    for s in ps:
        if lp * s > limit: break
        if s >= lp: break
        ans = 0
        for l in powers(lp, limit):
            if l * s > limit: break
            ans = max(ans, l * list(powers(s, limit / l))[-1])
        res += ans
print res

