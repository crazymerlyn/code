import numpy as np

N = 1 << 50
limit = int(N ** 0.5) + 1

is_prime = np.ones(limit + 1, dtype=np.bool_)
is_prime[0] = is_prime[1] = False
is_prime[4:limit+1:2] = False
for p in range(3, int(limit ** 0.5) + 1, 2):
    if is_prime[p]:
        is_prime[p * p:limit + 1:2 * p] = False

primes = np.where(is_prime)[0]

mu = np.ones(limit + 1, dtype=np.int8)
mu[0] = 0
for p in primes:
    mu[p::p] *= -1
    pp = p * p
    mu[pp::pp] = 0

total = 0
chunk = 100000
for start in range(1, limit + 1, chunk):
    end = min(start + chunk, limit + 1)
    i = np.arange(start, end, dtype=np.int64)
    m = mu[start:end]
    mask = m != 0
    if np.any(mask):
        total += np.sum(m[mask].astype(np.int64) * (N // (i[mask] * i[mask])))

print(total)
