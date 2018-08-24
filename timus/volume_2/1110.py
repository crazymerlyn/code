n, m, y = [int(x) for x in input().split()]

res = [x for x in range(m) if pow(x, n, m) == y % m]

if res: print(*res)
else: print(-1)
