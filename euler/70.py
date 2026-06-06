import math
LIMIT = 10**7
min_ratio = float('inf')
result = 0
phi = list(range(LIMIT + 1))
for i in range(2, LIMIT + 1):
    if phi[i] == i:
        for j in range(i, LIMIT + 1, i):
            phi[j] -= phi[j] // i
    if sorted(str(i)) == sorted(str(phi[i])):
        r = i / phi[i]
        if r < min_ratio:
            min_ratio = r
            result = i
print(result)
