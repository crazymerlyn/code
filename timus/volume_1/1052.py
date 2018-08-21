from collections import defaultdict
from fractions import Fraction
from math import ceil

def get_line(a, b):
    if a[0] != b[0]:
        m = Fraction((a[1] - b[1]), (a[0] - b[0]))
        c = a[1] - m * a[0]
        return (m.numerator, m.denominator, c.numerator, c.denominator)
    else:
        return a[0]

n = int(input())
ps = []

for _ in range(n):
    ps.append([int(x) for x in input().split()])

res = 0
for i in range(n-1):
    lines = defaultdict(int)
    for j in range(i + 1, n):
        p = ps[i]
        p2 = ps[j]
        if p == p2: continue
        lines[get_line(p, p2)] += 1
    x = max(lines.values()) + 1
    res = max(res, x)

print(res)
