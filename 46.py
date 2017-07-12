def primes(n):
    is_prime = [True] * (n+1)
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [m for m in range(2, n+1) if is_prime[m]]

ps = [p for p in primes(10000) if p > 999]
n = len(ps)

for i in range(n):
    for j in range(i+1, n):
        p1 = ps[i]
        p2 = ps[j]
        if 2*p2 - p1 not in ps: continue
        p3 = 2*p2 - p1

        if sorted(str(p1)) == sorted(str(p2)) == sorted(str(p3)):
            print p1, p2, p3


