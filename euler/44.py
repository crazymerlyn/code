def is_pentagonal(x):
    n = int((2 * x / 3) ** 0.5) + 1
    return n * (3 * n - 1) // 2 == x

pent = [n * (3 * n - 1) // 2 for n in range(1, 10000)]
best = None

for i in range(len(pent)):
    for j in range(i + 1, len(pent)):
        s = pent[i] + pent[j]
        d = pent[j] - pent[i]
        if is_pentagonal(s) and is_pentagonal(d):
            print(d)
            exit()
