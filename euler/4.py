best = 0
for a in range(100, 1000):
    for b in range(a, 1000):
        p = a * b
        s = str(p)
        if s == s[::-1] and p > best:
            best = p
print(best)
