from utils import primes
from itertools import combinations

def product(seq):
    res = 1
    for s in seq: res *= s
    return res

def muls(ps):
    res = []
    for i in range(len(ps)+1):
        for comb in combinations(ps, i):
            res.append(product(comb))
    return sorted(res)

ps = list(primes(190))
n = len(ps)

left = muls(ps[:n//2])
right = muls(ps[n//2:])

ans = 0
limit = product(ps) ** 0.5
from bisect import bisect_left
for val in left:
    i = bisect_left(right, limit / val)
    if i:
        ans = max(ans, val * right[i-1])
print(ans % 10 ** 16)

