from fractions import Fraction, gcd
from utils import memoized, factorize
from itertools import combinations
from collections import defaultdict

target = Fraction(1, 2)

def ss(xs):
    res = defaultdict(int)
    for i in range(len(xs) + 1):
        for comb in combinations(xs, i):
            s = sum(comb)
            if s <= target:
                res[s] += 1
    return res

t = 81
excluded = [16,27,32,48,54,64,65,80]
fs = [Fraction(1, x) ** 2 for x in range(2, t) if x not in excluded and all(p in [2, 3, 5, 7, 13] for p, _ in factorize(x))]

h = len(fs)//2

left = fs[:h]
right = fs[h:]

ss1 = ss(left)
ss2 = ss(right)

res = 0
for k, v in ss1.items():
    res += v * ss2[target-k]

print(res)

