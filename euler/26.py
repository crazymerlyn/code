best = 0
best_d = 0
for d in range(2, 1000):
    rem = 1
    seen = {}
    pos = 0
    while rem and rem not in seen:
        seen[rem] = pos
        rem = (rem * 10) % d
        pos += 1
    if rem:
        cycle = pos - seen[rem]
        if cycle > best:
            best = cycle
            best_d = d
print(best_d)
