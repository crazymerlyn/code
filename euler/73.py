from fractions import gcd
from math import ceil

res = 0
for d in range(4, 12001):
    for n in range(int(ceil(d/3.0)), d//2+1):
        if gcd(n, d) == 1:
            res += 1
print(res)
