n = 10**6

solution = [0 for _ in range(n+1)]

for u in range(1, n+1):
    for v in range(1, n/u + 1):
        if (u + v) % 4 == 0 and 3 * v - u > 0:
            solution[u*v] += 1

print sum(1 for x in solution if x == 10)

