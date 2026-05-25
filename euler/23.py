def is_abundant(n):
    total = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != 1 and i * i != n:
                total += n // i
    return total > n

limit = 28123
abundant = [i for i in range(12, limit) if is_abundant(i)]
can = [False] * (limit + 1)
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        s = abundant[i] + abundant[j]
        if s <= limit:
            can[s] = True
        else:
            break
total = sum(i for i in range(1, limit + 1) if not can[i])
print(total)
