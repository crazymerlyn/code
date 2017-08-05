from utils import primes

ps = primes(10000)
min_ratio = float('inf')
ans = None
for p1 in ps:
    for p2 in ps:
        if p1 == p2: continue
        phi = (p1 - 1) * (p2 - 1)
        n = p1 * p2
        if n >= 10**7: break
        if sorted(str(n)) == sorted(str(phi)):
            ratio = 1.0*n / phi
            if ratio < min_ratio:
                min_ratio = ratio
                ans = n
print ans

