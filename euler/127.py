from fractions import gcd
from utils import memoized, primes
from utils import factorize

def product(seq):
    return reduce(lambda x,y:x*y, seq, 1)

limit = 120000

radicals = []

for i in range(1, limit+1):
    radical = product(p for p, _ in factorize(i))
    radicals.append((radical, i))


sortedRadicals = sorted(radicals)
radicals = [0] + [radical for radical, _ in radicals]

s = 0
for c in range(1, limit):
    for arad, a in sortedRadicals:
        if arad * radicals[c] > c / 2: break
        if gcd(a, c) > 1: continue
        b = c - a
        if b < a: continue
        if arad * radicals[b] * radicals[c] < c: s += c
print s

