from math import gcd

limit = 1000
solutions = [0] * (limit + 1)

for m in range(2, int(limit ** 0.5) + 1):
    for n in range(1, m):
        if (m - n) % 2 == 0 or gcd(m, n) != 1:
            continue
        a = m * m - n * n
        b = 2 * m * n
        base = 2 * m * (m + n)
        if base > limit:
            break
        for k in range(1, limit // base + 1):
            solutions[k * base] += 1

best_p = max(range(limit + 1), key=lambda i: solutions[i])
print(best_p)
