LIMIT = 1000000
phi = list(range(LIMIT + 1))
for i in range(2, LIMIT + 1):
    if phi[i] == i:
        for j in range(i, LIMIT + 1, i):
            phi[j] -= phi[j] // i
print(max(range(2, LIMIT + 1), key=lambda n: n / phi[n]))
