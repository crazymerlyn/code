def primes(n):
    is_prime = [True] * (n+1)
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [m for m in range(2, n+1) if is_prime[m]]

ps = primes(1000000)

p_set = set(ps)
res = 0
for n in range(21, 1000, 2):
    sums = [0 for _ in ps]
    m = 0
    for i, p in enumerate(ps):
        sums[i] += p
        if i > 0: sums[i] += sums[i-1]
        if i >= n: sums[i] -= ps[i-n]
        else: continue
        if sums[i] in p_set and m < sums[i]:
            m = sums[i]
    if m:
        print n, m
        res = m

print "Answer:", m

