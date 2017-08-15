from utils import primes

limit = 10**10
for i, p in enumerate(primes(10**6)):
    n = i + 1
    if n % 2 == 0: continue

    r = 2 * p * n % (p * p)

    if r > limit:
        print n
        break

