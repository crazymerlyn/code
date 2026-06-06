from math import comb
print(sum(1 for n in range(1, 101) for r in range(1, n+1) if comb(n, r) > 1000000))
