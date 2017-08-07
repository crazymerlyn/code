from collections import defaultdict
from fractions import gcd

limit = 15 * 10 ** 5

mlimit = int((limit//2) ** 0.5)
seen = defaultdict(int)
for n in range(1, mlimit):
    for m in range(n+1, mlimit):
        if gcd(m*m-n*n, m*m+n*n) != 1: continue
        l = 2 * m * (m + n)
        x = l
        while x <= limit:
            seen[x] += 1
            x += l
print sum(1 for x in seen if seen[x] == 1)
