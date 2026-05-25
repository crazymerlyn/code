def primes(n):
    is_prime = [True] * (n + 1)
    ps = []
    for i in range(2, n + 1):
        if is_prime[i]:
            ps.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return ps

ps = primes(2000)
best_n = 0
best_ab = 0
for a in range(-999, 1000):
    for b in ps:
        if b > 1000:
            break
        n = 0
        while True:
            v = n * n + a * n + b
            if v < 2 or v not in ps:
                break
            n += 1
        if n > best_n:
            best_n = n
            best_ab = a * b
print(best_ab)
