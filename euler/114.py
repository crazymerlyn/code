
m, n = 3, 50
ways = [1]*(m) + [0]*(n-m+1)
for k in range(m, n+1):
    ways[k] = ways[k-1] + sum(ways[:k-m]) + 1

print ways[n]
